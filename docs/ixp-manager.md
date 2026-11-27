# IXP Manager integration

Status: proposed, not deployed.

Use IXP Manager (https://www.ixpmanager.org/) as the candidate administrative source of truth for µIX participants, ASNs, interfaces, VLANs, peering addresses and route-server configuration generation. Keep the existing isolated BIRD lab as the regression environment. Verify supported BIRD versions and configuration templates against the selected IXP Manager release before integration.

## Architecture

- Management application and database on a private management network, separate from the peering LAN.
- RS1 and RS2 retain independent configuration deployment and rollback.
- Prometheus/Grafana remain operational monitoring components; evaluate supported traffic statistics integrations separately.
- Public participant information is explicitly approved; credentials and private contact details are never committed.

## Pilot

1. Select a supported release and follow upstream installation requirements in a disposable environment.
2. Create a synthetic exchange, peering VLAN, two route servers and three participants using existing lab ASNs and documentation addresses.
3. Generate candidate configurations and compare them against existing lab policy. Do not overwrite working configurations automatically.
4. Verify syntax, dual-stack sessions, prefix and origin authorization, ROV, prefix limits, selective export and failover using existing tests.
5. Stage changes one route server at a time, with explicit approval and last-known-good rollback.
6. Test backup and restore of the database and configuration, administrative access controls and participant onboarding/offboarding.

## Acceptance gates

- No loss of existing security policy or regression coverage.
- No production credentials or public peering connectivity in the pilot.
- Generated configurations reproducible and reviewable.
- Documented supported versions, upgrade procedure and rollback.

Live installation, template compatibility, API integration and operational acceptance remain pending. This document is not a claim that upstream templates implement every existing lab policy.
