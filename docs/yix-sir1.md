# YIX-SIR1 — Sirdal technical design

Status: proposal; no site, carrier, equipment or production resources confirmed.

## Scope

A small carrier-neutral exchange hosted initially in the proposed Ploos micro data centre in Sirdal, Norway. Separate exchange governance, participant access and network policy from Ploos hosting and IP transit. Start with one or two shared facility racks, not dedicated full racks for the exchange.

## Logical topology

```text
Participant A ----+                    +---- Participant B
                  |                    |
             Peering SW1 ======== Peering SW2
                  |                    |
                 RS1                  RS2
                  |                    |
             Separate management network
                  |                    |
             Monitoring / IXP Manager / RPKI
```

Route servers exchange control-plane information only; participant traffic traverses the Layer 2 peering fabric directly. The inter-switch connection is a planned redundant logical link, subject to loop prevention and failure testing. Single-homed participants remain vulnerable to their access switch failing.

## Phase 1

- One managed switch with SFP+ 10GbE ports and suitable uplink capacity; second switch when justified or before offering fabric redundancy.
- Two independent route-server hosts or isolated VMs on separate physical hosts.
- 1/10GbE participant interfaces subject to optics and switch compatibility; evaluate 25/100GbE expansion later.
- Dedicated peering VLAN with IPv4 and IPv6; no default gateway, DHCP or facility management services on the peering LAN.
- Separate management network with restricted access, monitoring and configuration backups.
- Independent RPKI validation design; do not use the synthetic lab RTR service in production.
- Documented MAC limits, broadcast controls, permitted Ethernet protocols and participant isolation policy compatible with direct peering.

## Facility dependencies

Survey power, UPS, cooling, fire detection, physical access, grounding, fibre entrances and carrier availability. Seek diverse fibre paths and independent power feeds where feasible. Two switches in one rack do not establish site redundancy. Do not claim independent carrier paths until verified.

## Addressing and administration

Obtain appropriate public ASN and peering LAN address resources through the applicable RIPE NCC process; verify eligibility and costs. Private ASNs and documentation prefixes remain lab-only. Evaluate IXP Manager as source of truth, BIRD route servers, RPKI validators and Prometheus/Grafana. Ploos hosting, transit and exchange services must use distinct logical networks and published terms.

## Acceptance gates

- Confirm site, power, fibre and at least two independent prospective participant networks.
- Verify resource allocation, peering policy, participant agreements and operational responsibilities.
- Validate switch forwarding, MTU, MAC limits, IPv4/IPv6, route filtering, max-prefix, ROV and community behavior.
- Test route-server and switch failure separately, management isolation, backup restoration and monitoring alerts.
- Publish only verified capabilities and service availability.

## Open decisions

Site and rack layout; switch models and port count; optics and fibre paths; power budget; public ASN and addresses; pricing and governance; operational staffing and support hours. No equipment purchase or production deployment is authorized by this proposal.
