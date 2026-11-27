# YIX-SIR1 equipment and investment budget

Planning estimates in NOK excluding VAT, not supplier quotations or verified market prices. Incremental exchange equipment only; facility and carrier costs excluded. No procurement authorization.

| Item | Micro | Standard | Growth |
|---|---:|---:|---:|
| Managed peering switches | 4,000–10,000 | 10,000–24,000 | 30,000–90,000 |
| Two independent route-server hosts | 3,000–6,000 | 6,000–12,000 | 10,000–20,000 |
| Management switching | 1,000–3,000 | 2,000–5,000 | 4,000–10,000 |
| Optics, DACs and patch cables | 2,000–5,000 | 5,000–12,000 | 12,000–35,000 |
| Spares and mounting accessories | 2,000–4,000 | 4,000–8,000 | 8,000–20,000 |
| Subtotal | 12,000–28,000 | 27,000–61,000 | 64,000–175,000 |
| Total with 20% contingency | 14,400–33,600 | 32,400–73,200 | 76,800–210,000 |

These are alternative complete equipment scenarios, not cumulative upgrade prices. Reuse can reduce incremental costs.

## Procurement criteria

Micro: one managed 10GbE switch, two independent route-server hosts, separate management. Standard: two switches, tested interconnect and separate power feeds where available. Growth: evaluate 25/100GbE based on committed participant demand. Single-homed participants are not fabric redundant.

Candidate used equipment families for evaluation, not approved models: MikroTik CRS317/CRS326-24S+2Q+, enterprise Arista or Juniper switches, Dell OptiPlex Micro / Lenovo ThinkCentre Tiny / HP EliteDesk Mini for route servers. Verify exact SKU, firmware support, licensing, airflow, power, optics compatibility, MTU, MAC limits, storm control, VLAN isolation, management security and spare availability. Avoid unsupported firmware and mandatory unavailable licenses. Test actual forwarding and failure behavior before purchase commitments.

## Operating costs

Estimate annual electricity as measured watts × 8.76 × effective NOK/kWh. For example, 150 W at NOK 1.50/kWh is NOK 1,971/year before cooling and facility overhead. Measure actual load. Separately obtain quotes for fibre, cross-connects, public number resources, support, replacement stock, insurance and allocated facility costs. Do not treat these as zero.

## Decision gates

Confirm at least two independent prospective participant networks, site and carrier availability, resource eligibility, operating budget and governance. Buy only pilot equipment after approval. Obtain multiple quotations including shipping and VAT treatment. Do not offer redundancy or live peering before acceptance testing.

No current supplier pricing, site survey or procurement approval has been obtained.
