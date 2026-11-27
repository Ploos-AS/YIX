# µIX — Micro Internet eXchange

**Small exchange. Big connections.**

An open framework for small, distributed Internet Exchanges, initiated by Ploos AS.

µIX (ASCII: YIX) aims to enable independent operators to establish affordable, carrier-neutral local and regional peering points using existing Internet standards, reusable configurations, operational guidance and conformance tests.

## Principles

Open specification, open source, vendor neutrality, carrier neutrality, decentralized operation and commercial freedom. No mandatory central infrastructure, Ploos service purchase or framework licensing fees. Each exchange operates independently; inter-site connectivity is optional and must not imply a shared Layer 2 failure domain.

## Scope

Ethernet peering LANs, IPv4/IPv6 bilateral and optional route-server peering, BGP hygiene, RPKI, IRR filtering, monitoring, onboarding, security and reproducible deployment. Proposed Nano, Micro and Regional profiles will be specified and tested separately.

## First planned physical reference implementation

YIX-SIR1 in Sirdal, Norway, is the first planned physical implementation, initially proposed for a future Ploos micro datacenter. No live fabric, participants, ASN, production service or SLA is claimed. Site-specific choices are not universal requirements.

## Project status

Early development; not a ratified industry standard. The virtual lab and existing site documentation are inputs to the future versioned specification.

- [Architecture](docs/architecture.md)
- [Peering policy](docs/peering-policy.md)
- [Roadmap](ROADMAP.md)
- [Security](SECURITY.md)
- [Licensing policy](LICENSING.md)

Website: https://yix.no (publication pending verification).

## Relationship to Ploos

Ploos AS initiates the framework and proposes to operate SIR1. Independent implementations need not purchase Ploos services. The project is distinct from Ploos Datacenter, Ploos VPS and QIX/IIX URL shortening.

## Contributions

Feedback and contributions are welcome. Do not publish secrets, production configurations or sensitive participant data.
