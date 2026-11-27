# YIX-SIR1 operations and security runbook

Draft for pilot approval; not a claim of operational readiness or a 24/7 staffed NOC.

## Responsibilities and support

Assign primary and backup operators, emergency contacts and escalation paths before activation. Publish actual support hours and maintenance procedures. Do not promise response times or availability without approved staffing and service terms.

## Routine operations

| Frequency | Checks |
|---|---|
| Daily | Review alerts, BGP sessions, RPKI cache freshness, port errors and resource utilization |
| Weekly | Review unresolved incidents, configuration changes, backup results and security advisories |
| Monthly | Review access, patch status, capacity, participant contacts and sample backup restoration |
| Quarterly | Exercise route-server failover, incident response and configuration recovery |
| Annually | Review governance, supplier dependencies, disaster recovery and service commitments |

Automate checks where feasible; assign ownership and record evidence. Monitoring should cover switch health, link state, BGP sessions, prefix counts, RPKI freshness, host resources and backup status. Use the existing Prometheus/Grafana lab as a starting point, subject to production validation.

## Security baseline

Separate management from the peering fabric. Restrict management access via authenticated VPN or dedicated management network, least privilege and MFA where supported. Use individual accounts, SSH keys, secure secret storage and audited changes. Disable unused services and ports. Maintain supported firmware and operating systems. Never store production credentials in Git.

Apply approved peering filters, prefix limits and layer-2 protections. Validate changes in the lab before production. Require a documented rollback plan and independent review for high-risk changes where feasible.

## Incident response

Classify incidents as critical fabric/security outage, degraded service or routine issue. Record detection, impact, owner and actions. For route leaks or disruptive traffic, isolate affected sessions or ports proportionately under the approved policy, preserve evidence, notify affected participants and restore only after validation. Escalate facility, carrier and security incidents to appropriate contacts. Assess applicable notification obligations. Conduct a post-incident review and track corrective actions.

## Backup and recovery

Back up switch and route-server configurations, policy data and essential operational records after changes and on a scheduled basis. Encrypt backups, keep an independent off-site copy and restrict access. Test restoration on spare or isolated equipment. Define and approve recovery objectives and retention periods before launch. Maintain a documented inventory and spare strategy.

## Pilot acceptance

Verify monitoring and alert delivery, access controls, configuration restore, route-server failover, participant isolation, rollback and contact escalation. Record test evidence and unresolved risks. A single-switch pilot remains a single point of failure. No production SLA, staffing commitment or completed acceptance test is established by this document.
