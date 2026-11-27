# RPKI validation plan

The lab currently uses exact per-participant prefix and first/origin ASN checks. These are synthetic authorization rules, not RPKI. The negative smoke test advertises unauthorized documentation prefixes and checks that neither route server nor other participants accepts them. Wrong-origin rejection is configured but not independently exercised yet.

Next: add an isolated RTR fixture and BIRD ROA tables, test Valid, Invalid and NotFound separately, reject Invalid, and retain participant authorization checks for all states. Evaluate Routinator or another maintained validator for production, with redundant RTR endpoints and monitoring of freshness and outages. Never use synthetic lab authorizations in production. Define stale-cache and validator outage policy before launch.

## Static ROA fixture

Both route servers now use synthetic BIRD ROA tables. A's normal prefixes are Valid, B and C are NotFound, and A's additional test prefixes are explicitly authorized by the participant filter but Invalid against the fixture (different origin ASN). The smoke test checks export and rejection of these prefixes alongside existing positive tests. Static fixtures do not verify signed ROAs, RTR transport, cache freshness or dynamic revalidation. Never deploy these tables in production.
