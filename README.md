# µIX — Micro Internet eXchange

**Small exchange. Big connections.**

µIX (ASCII: **YIX**) is a proposed small-scale, carrier-neutral Internet Exchange Point (IXP) initiative by **Ploos AS**, intended to start at a future micro datacenter in **Sirdal, Norway**.

- Website: [yix.no](https://yix.no) (reserved for the project; no live service implied)
- Project name: **µIX — Micro Internet eXchange**
- Repository name and technical identifier: **YIX**
- Status: **concept / planning** — no exchange fabric, participants, ASN, or production peering service is claimed

## Purpose

Help independent networks exchange traffic locally through a neutral Layer 2 peering fabric. A future deployment could reduce unnecessary traffic detours and create a regional interconnection point, subject to demand, connectivity, funding, and operational readiness.

Ploos AS would operate the initial infrastructure; **neutral access and equal technical peering conditions** are design goals, not an assertion of independent governance.

## Scope

Initial planning covers:

- An Ethernet peering LAN with documented port and participant policies
- IPv4 and IPv6 bilateral peering, with optional route servers
- BGP routing hygiene, RPKI-based route validation, IRR-based filtering where appropriate, and monitoring
- Participant onboarding, maintenance, incident communication and public operational documentation
- A virtual lab to test designs before buying hardware

No live IP allocations, ASN, switch ports, member list, commercial pricing or uptime guarantees are defined yet.

## Documents

- [Architecture](docs/architecture.md)
- [Peering principles](docs/peering-policy.md)
- [Roadmap](ROADMAP.md)
- [Security and disclosure](SECURITY.md)

## Relationship to Ploos

µIX is a peering and interconnection initiative, distinct from Ploos Datacenter, Ploos VPS and the QIX/IIX URL-shortener SaaS products. Neither `yix.no` nor this repository is intended for URL shortening.

## Contributing

Architecture feedback and documentation contributions are welcome as the project matures. Do not post credentials, production configs, customer data or sensitive network details in public issues or commits.

© Ploos AS. Licensing for code and documentation will be determined before external reuse is invited.
