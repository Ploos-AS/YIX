# BGP Large Communities

Lab convention: `65000:0:<peer ASN>` suppresses export to that participant on both route servers. A tags its normal IPv4 and IPv6 prefixes with `65000:0:65002`, so B must not receive them while C still does. The convergence tests check this during normal operation and each route-server outage/recovery. Import authorization, ROV and prefix limits remain unchanged.

This is a private-ASN lab convention, not a published production policy. Production ASN assignment, reserved namespace handling, informational tags, allow-list overrides, well-known community policy and multiple-path behavior require further design and testing.
