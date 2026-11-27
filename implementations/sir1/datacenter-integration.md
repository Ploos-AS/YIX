# SIR1 and Ploos Datacenter integration

Status: proposed local integration, not deployed or contractually approved.
SPDX-License-Identifier: CC-BY-4.0

This document supplements the [SIR1 implementation record](README.md) and does not change the generic µIX specification. The [Ploos Datacenter repository](https://github.com/Ploos-AS/Ploos-Datacenter) is the proposed facility project; its current README does not establish facility capabilities.

## Responsibility boundaries

| Service | Proposed responsibility |
|---|---|
| Ploos Datacenter | Rack space, power, cooling, physical access, cross-connects and facility incidents |
| YIX-SIR1 | Peering fabric, participant admission, routing policy, exchange monitoring and exchange incidents |
| Ploos VPS | Virtual compute, separate customer and management networks |
| Ploos Hosting / Cloud / DNS | Application and infrastructure services outside the peering LAN |
| Potential Ploos Network | Separate commercial IP transit, if established |

Ploos AS may initially perform multiple roles, but should record separate service ownership, costs, access rules and incident responsibilities. No separate legal entity or existing transit service is asserted.

## Physical and logical handoff

Facility operator provides documented rack position, power budget, patch panel and cross-connect demarcation. Exchange operator owns switch port assignments, peering VLAN configuration, participant authorization and routing services. Participants retain control of their routers and BGP policy.

Keep facility management, VPS/customer traffic, transit and exchange management logically separate from the dedicated peering LAN. Do not use the exchange as a default gateway or carry unrelated customer traffic on it. Shared physical equipment requires documented isolation and failure domains. Two route-server VMs on one physical host are not independent.

## Neutral access

Publish equivalent technical and commercial exchange terms for equivalent participants, including affiliated Ploos networks. Participation must not require purchase of Ploos VPS, hosting, cloud or transit. Physical cross-connect or transport charges may apply transparently; assess external carrier and remote transport options without claiming availability. Ploos networks participating in the exchange must follow the same routing and admission policy. Route servers must not forward traffic or confer preferential transit.

## Facility readiness and acceptance

- Confirm rack space, electrical load, UPS, cooling, grounding, fire protection and physical access.
- Confirm fibre entrances, carrier availability, cross-connect demarcation and actual diversity.
- Document shared power, switch, host and management failure domains.
- Agree incident ownership, escalation, maintenance notification, access and cost allocation.
- Verify management isolation, participant forwarding, dual-stack peering, applicable route-server policy, monitoring and restoration.
- Record evidence against the Nano profile and baseline specification before any conformance claim.

Use the existing SIR1 readiness gates; all remain pending until evidence is recorded. No SLA, hardware procurement, facility reservation, carrier agreement or production deployment is authorized here.

## Future integration

A separate facility-side interface document may be proposed in Ploos Datacenter once its design is established. Keep generic µIX tooling independent of Ploos infrastructure and avoid hard-coded facility dependencies. Other operators may choose any suitable facility.
