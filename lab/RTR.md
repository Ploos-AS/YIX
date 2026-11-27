# RTR fixture

The isolated Python service supplies four synthetic VRPs over RTR v1 to both BIRD route servers. CI checks that the ROA tables populate and retains the existing valid, uncovered, invalid and failover checks. The fixture uses a fixed serial and does not fetch or validate signed objects. Dynamic serial changes, cache outage/expiry tests, redundant validators and production security remain future work. The fixture is not suitable for production.
