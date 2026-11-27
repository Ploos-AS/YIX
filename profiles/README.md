# µIX deployment profiles v0.1

Working draft. SPDX-License-Identifier: CC-BY-4.0

All profiles inherit [µIX Specification v0.1](../specification/v0.1.md). BCP 14 terminology applies. Profile requirements add to, and never waive, baseline requirements. Participant counts and port speeds below are illustrative planning targets, not conformance thresholds.

| Profile | Indicative participants | Typical ports | Fabric | Route servers |
|---|---:|---|---|---|
| Nano | 2–5 | 1/10 GbE | Single switch permitted | Optional |
| Micro | 5–25 | 1/10/25 GbE | One or more switches | Two independent instances required |
| Regional | 20–100+ | 10/25/100 GbE | Redundant fabric required | Two or more independent instances required |

## Nano

- NANO-01: A single-switch fabric MAY be used; the single point of failure MUST be disclosed.
- NANO-02: Route servers MAY be omitted. If offered, all conditional baseline requirements apply.
- NANO-03: Operators MUST maintain documented recovery procedures and basic monitoring satisfying OPS requirements.

## Micro

- MICRO-01: At least two route-server instances MUST be offered in independent host failure domains; participation remains optional.
- MICRO-02: Fabric redundancy SHOULD be provided; a single-switch design MUST disclose its failure domain.
- MICRO-03: Operators MUST monitor route-server health independently and test failover before production activation.

## Regional

- REG-01: The fabric MUST provide redundant switching paths and documented failure domains. Participant attachment redundancy MUST be documented separately.
- REG-02: At least two route servers MUST be offered across independent host failure domains.
- REG-03: Operators MUST test switch and route-server failure scenarios and document capacity during degraded operation.
- REG-04: Management and alerting SHOULD remain available during a single fabric failure.

## Profile transitions

Operators SHOULD preserve participant addressing and peering policy where practical, and MUST validate changes and document outages. Upgrades do not automatically require new ASNs or peering prefixes. A profile claim requires evidence for the baseline and all applicable profile requirements. Profile names do not imply an SLA, site diversity or independent certification.

## SIR1

Sirdal is the first planned physical reference implementation. Nano is the proposed initial target; Micro is a possible expansion after demand, funding and independent route-server hosts are confirmed. No profile conformance is claimed.

## Validation

Future conformance tests must map each identifier to evidence, including topology review, monitoring, recovery and failover where applicable. No tests have been executed by this document.
