#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
trap 'docker compose ps -a; docker compose logs; docker compose down --volumes' EXIT
docker compose config --quiet
docker compose build
for node in rs rs2 a b c; do
  docker compose run --rm --no-deps "$node" bird -p -c /etc/bird/bird.conf
done
docker compose up -d
ready() {
  local active="$1" node output expected
  shift
  for node in "$@"; do
    output=$(docker compose exec -T "$node" birdc show protocols) || return 1
    [[ $(grep -c 'Established' <<< "$output") -eq 6 ]] || return 1
  done
  for node in a b c; do
    output=$(docker compose exec -T "$node" birdc show protocols) || return 1
    expected=$((active * 2))
    [[ $(grep -c 'Established' <<< "$output") -eq "$expected" ]] || return 1
    output=$(docker compose exec -T "$node" birdc show route all) || return 1
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
