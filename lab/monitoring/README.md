# Optional lab monitoring

From lab/ run `docker compose -f compose.yaml -f monitoring/compose.yaml up --build -d`. Grafana is available on localhost:3000 and Prometheus on localhost:9090. Set a strong GRAFANA_PASSWORD environment variable before starting. Query `muix_bgp_session_up`, `muix_bird_routes`, and `up{job="muix"}`. Route counts include paths, not necessarily unique prefixes. Stop using the same two Compose files and `down`.

The exporters use BIRD's restricted client mode, but the shared socket is not a security boundary; this is an isolated lab only. Production requires a restricted server-side socket, authenticated management network, alerts and access controls. The optional overlay is not exercised by the existing BGP smoke test. Runtime verification remains pending.
