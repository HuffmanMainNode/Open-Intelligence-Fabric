# Security Policy

The Fabric defines descriptive contracts. It is not an authorization system or a secure execution environment.

- Treat resource manifests, capability declarations, URLs, and publisher metadata as untrusted.
- A manifest's permissions field never grants access.
- Consumers must independently authenticate publishers and verify artifact provenance.
- Enforce authorization at invocation time and isolate execution.
- Do not publish secrets, private endpoints, or personal data in manifests.
- Schema validation confirms structure only, not truth, safety, or capability.

Report vulnerabilities privately to the maintainers with affected revision, impact, and a minimal reproduction. Do not include credentials or private data.
