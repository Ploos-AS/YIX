# µIX — Micro Internet eXchange

**Small exchange. Big connections.**

An open framework for small, distributed Internet Exchanges, initiated by Ploos AS.

µIX (ASCII: YIX) aims to enable independent operators to establish affordable, carrier-neutral local and regional peering points using existing Internet standards, reusable configurations, operational guidance and conformance tests.

## Principles

Open specification, open source, vendor neutrality, carrier neutrality, decentralized operation and commercial freedom. No mandatory central infrastructure, Ploos service purchase or framework licensing fees. Each exchange operates independently; inter-site connectivity is optional and must not imply a shared Layer 2 failure domain.

## Scope

Ethernet peering LANs, IPv4/IPv6 bilateral and optional route-server peering, BGP hygiene, RPKI, IRR filtering, monitoring, onboarding, security and reproducible deployment. Draft Nano, Micro and Regional profiles are defined; validation remains incomplete.

## First planned physical reference implementation

YIX-SIR1 in Sirdal, Norway, is the first planned physical implementation, initially proposed for a future Ploos micro datacenter. No live fabric, participants, ASN, production service or SLA is claimed. Site-specific choices are not universal requirements.

## Project status

Preparing v0.1.0-alpha; not a ratified industry standard or production-ready release. The draft specification and lab are available; physical conformance is unverified.

- [Specification v0.1](specification/v0.1.md)
- [Profiles](profiles/README.md)
- [Reference architecture](architecture/reference-v0.1.md)
- [SIR1](implementations/sir1/README.md)
- [Toolkit](toolkit/README.md)
- [Conformance](conformance/README.md)
- [Governance](GOVERNANCE.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [Lab architecture](docs/architecture.md)
- [Peering policy](docs/peering-policy.md)
- [Roadmap](ROADMAP.md)
- [Security](SECURITY.md)
- [Licensing policy](LICENSING.md)

Website: https://yix.no (publication pending verification).

## Relationship to Ploos

Ploos AS initiates the framework and proposes to operate SIR1. Independent implementations need not purchase Ploos services. The project is distinct from Ploos Datacenter, Ploos VPS and QIX/IIX URL shortening.

## Contributions

Feedback and contributions are welcome. Do not publish secrets, production configurations or sensitive participant data.
