# IRR and prefix limits

Both lab route servers apply per-address-family receive and import limits. A receives at most four routes and imports at most two; B and C receive at most two and import at most one. Exceeding either limit disables the affected channel/protocol; operator intervention is expected. These are synthetic lab thresholds, not production defaults.

Production filters should be generated from participant-approved AS-SETs and trusted IRR sources, with bounded recursion, explicit prefix-length constraints, origin authorization and independent RPKI Invalid rejection. Validate generated configuration, review diffs, retain last-known-good filters, and stage deployment across route servers. Never replace filters with permit-all on lookup failure. Establish per-participant IPv4/IPv6 limits during onboarding and monitor utilization.

Live IRR retrieval, filter generation and deliberate limit-exceedance tests are not implemented in this change. Existing smoke tests verify normal operation under the limits.
