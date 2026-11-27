# yix.no public website launch

Publish the existing bilingual static website as a project announcement, not an operational exchange. Proposed host: Forseti, subject to capacity and deployment approval.

## Preflight
- Inspect the existing website files and verify both language versions, navigation, accessibility and mobile layout.
- Clearly label the exchange as planned / under development in Sirdal, Norway. Do not publish unapproved pricing, participant names, ASN, service availability or SLA.
- Verify a working contact channel before inviting interest; do not invent an email address.
- Check existing DNS records and any legacy URL-shortener traffic. Preserve required MX/TXT records and agree migration or retirement of legacy links before changing web DNS.

## Deployment
Use a dedicated static document root containing only reviewed website assets, not the repository, lab configurations or internal documents. Deploy a reviewed commit using the existing Ploos deployment process or a separately approved static Caddy configuration. Proposed canonical host yix.no, with www.yix.no redirect after DNS and TLS verification. Keep previous release available for rollback. No backend or tracking is required for the initial site.

## Acceptance
Validate DNS A/AAAA as applicable, HTTPS certificate, canonical redirect, both languages, asset loading, 404 behavior and absence of exposed repository files. Verify from an external network. Configure HTTP monitoring and document release commit and rollback procedure.

No DNS changes, server deployment, contact setup or external validation have been performed by this PR. Confirm target host, actual website path and legacy traffic before execution.
