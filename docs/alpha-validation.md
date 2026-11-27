# Alpha validation record

Baseline before this PR: 2d16c44505768bc4d351847052f76a877a55b207.

Previous PR #34 toolkit workflow run 46058684808 succeeded. The connector returned no PR-triggered runs for the baseline main commit; this does not establish push CI status.

This PR triggers BGP smoke testing and adds offline README/website link checks to toolkit CI. Record actual candidate results after CI completes and again after merge.

## Coverage and limitations

- Toolkit: unit tests and three example inventories; not deployment or physical topology verification.
- BGP smoke: BIRD configuration parsing, synthetic dual-stack route-server sessions, individual route-server outages/recovery, unauthorized prefixes, synthetic RPKI Invalid rejection and selective export.
- Link checks: README and website local targets, including repository main-branch documentation links resolved locally. No external availability, anchors, browser accessibility or visual checks.
- Not verified by these checks: independent BGP implementations, bilateral interoperability, real RPKI/IRR feeds, monitoring overlay, physical redundancy, production security or conformance.
- License provenance remains pending per alpha-provenance-review.md.

## Release decision

Do not tag until candidate CI, manual rights review and remaining release checklist items are resolved or explicitly documented where the checklist permits. No production claim or release is created here.
