#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
trap 'docker compose logs; docker compose down --volumes' EXIT
docker compose config --quiet
docker compose build
for node in rs a b c; do
  docker compose run --rm --no-deps "$node" bird -p -c /etc/bird/bird.conf
done
docker compose up -d
ready() {
  local node expected output
  for node in rs a b c; do
    expected=2
    [[ "$node" != rs ]] || expected=6
    output=$(docker compose exec -T "$node" birdc show protocols) || return 1
    [[ $(grep -c 'Established' <<< "$output") -eq "$expected" ]] || return 1
  done
  for node in a b c; do
    output=$(docker compose exec -T "$node" birdc show route all) || return 1
    for prefix in 198.51.100.0/26 198.51.100.64/26 198.51.100.128/26 2001:db8:11::/48 2001:db8:12::/48 2001:db8:13::/48; do
      grep -Fq "$prefix" <<< "$output" || return 1
    done
  done
}
for attempt in $(seq 1 60); do
  if ready; then
    echo "All BGP sessions and expected prefixes verified"
    exit 0
  fi
  sleep 2
done
echo "BGP convergence timed out" >&2
exit 1
