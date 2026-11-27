# Isolated µIX BGP lab

Requires Docker Compose with IPv6 bridge support. From this directory run `docker compose up --build -d`. No ports are published; the peering bridge is internal. Image building requires package repository access.

Inspect `docker compose exec rs birdc show protocols` and `docker compose exec a birdc show route all`. Expect six established sessions on rs and two on each participant, with the other two participants' synthetic prefixes visible in each address family. Routes are control-plane examples only; no kernel route installation or forwarding is configured. Stop with `docker compose down`.

Private ASNs and documentation prefixes are used. The route server accepts only the exact synthetic prefix assigned to each participant. This is not production policy or a complete RPKI implementation. Runtime validation is pending.
