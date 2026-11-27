# Peering principles — draft

This is a **discussion draft**, not an offer of service or an active participant agreement.

## Neutrality

µIX aims to offer fair technical access to eligible networks regardless of whether they purchase hosting or transit from Ploos AS. Participants choose their own peering relationships. Joining the fabric does not automatically create BGP peering with other members.

## Traffic exchange

- The shared fabric is for IP interconnection between participating autonomous networks.
- Participants should maintain accurate routing contacts and prefix/ASN information.
- Route-server participation, if offered, is opt-in; bilateral peering remains possible.
- Participants are responsible for their own routing and filtering policies.
- Unsolicited Layer 2 control traffic, loops, spoofing and activity disrupting other participants are prohibited; exact technical limits will be published before launch.

## Routing safeguards

- Prefer explicit route-server import/export policies and validated origin information.
- Evaluate RPKI origin validation and current IRR records without treating either as a complete routing-security solution.
- Implement maximum-prefix limits and sane session defaults with documented escalation procedures.
- Avoid announcing default routes or offering transit through route servers.

## Operations and transparency

Before any service goes live, publish port requirements, acceptable-use rules, maintenance notices, incident contacts, participant onboarding steps and a clear privacy policy. Commercial terms and service levels are **not yet defined**.

## Not in scope

µIX is not an ISP, internet transit provider, URL-shortener platform or guarantee that participants can reach the entire internet through the exchange.
