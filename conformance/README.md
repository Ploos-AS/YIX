# µIX conformance framework v0.1

Working draft. SPDX-License-Identifier: CC-BY-4.0

Use with specification/v0.1.md and profiles/README.md. This is self-assessment, not certification. The matrix covers 21 baseline and 10 profile requirement IDs. Each row is a minimum evidence prompt; assess every normative clause in the source, including unnumbered transition and claim requirements.

| Requirement | Applicability | Evidence / procedure |
|---|---|---|
| ARCH-01 | all | Inspect fabric diagram; attempt management access from authorized lab participant port; verify blocked. |
| ARCH-02 | all | Establish bilateral IPv4 and IPv6 sessions and verify documented MTU, addressing and port settings. |
| ARCH-03 | all | Review dependencies; demonstrate operation without central µIX or Ploos services. |
| ARCH-04 | inter-site | Review inter-site failure domains and responsibility records. |
| ARCH-05 | single-switch | Verify published single-switch limitation. |
| PEER-01 | all | Review onboarding authorization and legitimate resource records. |
| PEER-02 | all | Demonstrate bilateral BGP without route server; verify optional participation. |
| PEER-03 | all | Review published access criteria and equivalent treatment records. |
| PEER-04 | all | In isolated lab verify port controls, authorized ARP/ND and rejection of unauthorized DHCP and gateway services. |
| PEER-05 | all | Review participant route authorization and sampled announcements. |
| RS-01 | route-server | Verify next-hop preservation, RFC 7947 behavior and no participant data forwarding. |
| RS-02 | route-server | Inject synthetic wrong-first-AS and excess prefixes; verify enforcement and documented exceptions. |
| RS-03 | route-server | Exercise Valid, Invalid, NotFound and cache loss; verify rejection and documented behavior. |
| RS-04 | route-server | Exercise authorized and unauthorized prefixes; inspect data provenance and update automation or justification. |
| RS-05 | route-server | Test selective export and community policy with multiple synthetic peers. |
| RS-06 | route-server | Inspect host failure domains and redundancy disclosure; justify SHOULD deviations. |
| OPS-01 | all | Review contacts, incident and rollback procedures. |
| OPS-02 | all | Trigger fabric and applicable routing alerts; verify metrics and RPKI freshness. |
| OPS-03 | all | Review authentication, access restrictions, audit trail and MFA or justification. |
| OPS-04 | all | Restore protected backup in isolated environment and record outcome. |
| OPS-05 | all | Compare public service claims with verified evidence. |
| NANO-01 | nano/single-switch | Verify disclosure of single point of failure. |
| NANO-02 | nano | Record route-server applicability; apply RS tests if offered. |
| NANO-03 | nano | Review recovery procedures and monitoring evidence. |
| MICRO-01 | micro | Verify two independently hosted route servers and optional participation. |
| MICRO-02 | micro | Inspect switching redundancy or justified deviation and disclosure. |
| MICRO-03 | micro | Test independent monitoring and route-server failover. |
| REG-01 | regional | Inspect redundant paths, failure domains and participant attachment disclosure. |
| REG-02 | regional | Verify two independently hosted route servers. |
| REG-03 | regional | Exercise switch and route-server failure; record degraded capacity. |
| REG-04 | regional | Test management and alerting during single fabric failure or justify deviation. |

## Assessment rules

Record specification revision, profile, environment (lab or physical), topology revision, assessor, date and evidence references. Use PASS, FAIL, NOT_TESTED or NOT_APPLICABLE. Explain every exclusion; route-server tests cannot be excluded for Micro or Regional. A missing result or failed mandatory clause blocks a conformance claim. Document and justify SHOULD deviations separately; a justified SHOULD deviation does not waive a MUST. Do not equate lab success with physical readiness.

Perform disruptive tests only in an isolated lab or authorized maintenance window with rollback. Use synthetic routes and never leak test announcements to production. Sanitize public evidence.

## Interoperability

Exercise bilateral IPv4/IPv6 and optional multilateral sessions using independently implemented BGP stacks where available. Record software versions, expected and observed next hops, import/export results, communities, session recovery and MTU. Test each direction; repeat with a second implementation before claiming cross-vendor interoperability. No results are supplied here.

## Evidence template

Use assessment-template.json as a blank record; populate one result per applicable requirement and record explicit exclusions. No certification marks or automatic approval are granted.
