#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
trap 'docker compose ps -a; docker compose logs; docker compose down --volumes' EXIT
docker compose config --quiet
docker compose build
for node in rs rs2 a b c; do
  docker compose run --rm --no-deps "$node" bird -p -c /etc/bird/bird.conf
done
docker compose up -d rtr
docker compose up -d
ready() {
  local active="$1" node output expected
  shift
  for node in "$@"; do
    output=$(docker compose exec -T "$node" birdc show protocols) || return 1
    [[ $(grep -Ec '^[[:space:]]*[^[:space:]]+[[:space:]]+BGP[[:space:]].*Established' <<< "$output") -eq 6 ]] || return 1
    output=$(docker compose exec -T "$node" birdc show route table lab_roa4 all) || return 1
    local roa6
    roa6=$(docker compose exec -T "$node" birdc show route table lab_roa6 all) || return 1
    output="${output}"$'\n'"${roa6}"
    for prefix in 198.51.100.0/26 192.0.2.128/25 2001:db8:11::/48 2001:db8:aaaa::/48; do
      grep -Fq "$prefix" <<< "$output" || { echo "$node: missing ROA $prefix" >&2; return 1; }
    done
  done
  for node in a b c; do
    output=$(docker compose exec -T "$node" birdc show protocols) || return 1
    expected=$((active * 2))
    [[ $(grep -Ec '^[[:space:]]*[^[:space:]]+[[:space:]]+BGP[[:space:]].*Established' <<< "$output") -eq "$expected" ]] || return 1
    output=$(docker compose exec -T "$node" birdc show route table master4 table master6 all) || return 1
    for prefix in 198.51.100.0/26 198.51.100.64/26 198.51.100.128/26 2001:db8:11::/48 2001:db8:12::/48 2001:db8:13::/48; do
      grep -Fq "$prefix" <<< "$output" || return 1
    done
  done
}
wait_ready() {
  for attempt in $(seq 1 60); do
    if ready "$@"; then return 0; fi
    sleep 2
  done
  echo "BGP convergence timed out: $*" >&2
  for node in "$@"; do
    docker compose exec -T "$node" birdc show protocols all || true
    docker compose exec -T "$node" birdc show route table lab_roa4 all || true
    docker compose exec -T "$node" birdc show route table lab_roa6 all || true
  done
  for node in a b c; do
    docker compose exec -T "$node" birdc show protocols || true
    docker compose exec -T "$node" birdc show route table master4 table master6 all || true
  done
  return 1
}
wait_ready 2 rs rs2
docker compose stop rs
wait_ready 1 rs2
docker compose start rs
wait_ready 2 rs rs2
docker compose stop rs2
wait_ready 1 rs
docker compose start rs2
wait_ready 2 rs rs2
echo "Both route-server outage and recovery scenarios passed"
for node in rs rs2; do
  for pair in 'a4 203.0.113.0/24' 'a6 2001:db8:ffff::/48'; do
    read -r proto prefix <<< "$pair"
    output=$(docker compose exec -T a birdc show route export "$([[ "$node" == rs ]] && echo "rs${proto:1}" || echo "rs2_${proto:1}")")
    grep -Fq "$prefix" <<< "$output"
  done
done
for node in rs rs2 b c; do
  output=$(docker compose exec -T "$node" birdc show route table master4 table master6 all)
  if grep -Eq '203\.0\.113\.0/24|2001:db8:ffff::/48' <<< "$output"; then
    echo "Unauthorized prefix accepted on $node" >&2
    exit 1
  fi
done
echo "Unauthorized IPv4 and IPv6 prefixes rejected"
for proto in rs4 rs2_4 rs6 rs2_6; do
  output=$(docker compose exec -T a birdc show route export "$proto")
  case "$proto" in
    *4) grep -Fq '192.0.2.128/25' <<< "$output" ;;
    *6) grep -Fq '2001:db8:aaaa::/48' <<< "$output" ;;
  esac
done
for node in rs rs2 b c; do
  output=$(docker compose exec -T "$node" birdc show route table master4 table master6 all)
  if grep -Eq '192\.0\.2\.128/25|2001:db8:aaaa::/48' <<< "$output"; then
    echo "ROA-invalid prefix accepted on $node" >&2
    printf '%s\n' "$output" >&2
    exit 1
  fi
done
echo "ROA-invalid prefixes rejected; valid and uncovered prefixes retained"
