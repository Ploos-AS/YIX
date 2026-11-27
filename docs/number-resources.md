# RIPE NCC and public number resources

Status: planning only. No resources requested or assigned.

## Resource separation

- Exchange peering LAN: dedicated IPv4 and IPv6 resources appropriate for an IXP, subject to current RIPE policy and eligibility.
- Route servers: evaluate a dedicated public ASN shared by redundant route servers.
- Ploos hosting/transit: separate operator ASN and address resources if required; never assume exchange LAN resources may be used for hosting or transit.
- Existing private ASNs and documentation prefixes remain isolated lab fixtures.

## Acquisition options

Compare direct RIPE NCC membership with a sponsoring LIR arrangement where permitted for each resource type. Verify current IXP assignment eligibility, ASN requirements, contractual obligations, fees, resource holder identity and ongoing reporting directly with RIPE NCC before selecting a path. Do not assume that sponsorship is available for every resource or that an ASN is automatically granted.

## Preparation checklist

1. Establish legal resource holder and operational contacts.
2. Document exchange purpose, planned location, topology and prospective independent participant networks.
3. Prepare IPv4/IPv6 addressing plan and route-server ASN justification.
4. Confirm current eligibility, application documents, costs and sponsorship options.
5. Define registry maintenance, abuse contacts, access control and resource lifecycle responsibilities.
6. Verify peering LAN routing policy, registry objects and applicable RPKI requirements before deployment. Do not originate the peering LAN globally by default.
7. Replace synthetic lab resources only in a separately reviewed production configuration after allocation.

## Official verification starting points

- https://www.ripe.net/ — current policies, resource requests and membership information.
- https://www.ripe.net/manage-ips-and-asns/ — resource management information.

Current fees and policy details have not been verified for this proposal. No membership, sponsorship, application or expenditure is authorized. Record verified policy references and quotations in a follow-up decision before applying.
