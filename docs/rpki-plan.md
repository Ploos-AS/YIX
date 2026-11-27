# RPKI validation plan

The lab currently uses exact per-participant prefix and first/origin ASN checks. These are synthetic authorization rules, not RPKI. The negative smoke test advertises unauthorized documentation prefixes and checks that neither route server nor other participants accepts them. Wrong-origin rejection is configured but not independently exercised yet.

Next: add an isolated RTR fixture and BIRD ROA tables, test Valid, Invalid and NotFound separately, reject Invalid, and retain participant authorization checks for all states. Evaluate Routinator or another maintained validator for production, with redundant RTR endpoints and monitoring of freshness and outages. Never use synthetic lab authorizations in production. Define stale-cache and validator outage policy before launch.
