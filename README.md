# Open Intelligence Fabric

**The shared contract layer for interoperable, inspectable Open Intelligence systems.**

Open Intelligence (OI) is an approach to open, interoperable, and verifiable intelligence systems in which models, agents, tools, datasets, computing resources, and human expertise can be discovered, evaluated, communicate, reason, coordinate, and contribute to shared objectives.

This repository is the ecosystem's standards and interoperability foundation. It defines common terms and resource descriptions. It does not host agents, execute tools, grant permissions, or provide a centralized intelligence service.

## What is implemented in v0.1.0

- A versioned core terminology vocabulary in `vocab/terms.json`.
- A machine-readable Intelligence Resource JSON Schema.
- A Python package for validating core resource manifests.
- An offline CLI: `oif-validate PATH/TO/manifest.json`.
- Unit tests for valid, invalid, and incomplete resource descriptions.
- A no-runtime-dependency package layout.

## Quick start

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
oif-validate examples/example-resource.json
```

## Intelligence Resource Contract

An OI Resource is a discoverable participant or asset: model, agent, tool, dataset, skill, service, compute resource, or human expertise offering. A manifest describes identity, publisher, version, capabilities, interfaces, inputs, outputs, permissions, provenance, verification, limitations, and license information.

Example:

```json
{
  "id": "example.text-summarizer",
  "name": "Example Text Summarizer",
  "resource_type": "tool",
  "publisher": {"name": "Example Publisher"},
  "version": "1.0.0",
  "capabilities": [{"id": "text.summarize"}],
  "permissions": [],
  "limitations": ["Example manifest; not a live service."]
}
```

The JSON Schema is the fuller contract. The initial Python validator intentionally checks a small stable core and does not yet implement every JSON Schema keyword.

## Core distinctions

- **OI**: the field and ecosystem.
- **OI Resource**: a discoverable model, agent, tool, dataset, skill, compute resource, or human expertise offering.
- **OI System**: a system that consumes, provides, coordinates, or evaluates resources.
- **OI Network**: connected OI systems and resources.
- **OI Fabric**: shared terminology, resource contracts, discovery conventions, and compatibility rules.
- **OI Swarm**: a coordinated population of distributed resources under an explicit objective and policy.
- **Federated Heterogeneous Mixture of Experts (FH-MoE)**: system-level selection and composition of independently implemented experts. This differs from a model's internal learned mixture-of-experts layers.

## Security and trust boundaries

Discovery is not authorization. A manifest's `permissions` field is descriptive and must never grant access by itself. Consumers must enforce authorization at invocation time, verify provenance, isolate execution, and treat all remote metadata as untrusted. A declared capability is a claim, not a measured guarantee.

## Ecosystem boundaries

- [OI Swarm Intelligence](https://github.com/HuffmanMainNode/OI-Swarm-Intelligence): policy-gated assignment planning.
- [OIF Research Observatory](https://github.com/HuffmanMainNode/OIF-Research-Observatory): source-backed research records.
- [OIF Model Intelligence](https://github.com/HuffmanMainNode/OIF-Model-Intelligence): model metadata and hardware-fit estimation.
- [OIF Cognitive Systems](https://github.com/HuffmanMainNode/OIF-Cognitive-Systems): planning and evidence-linked reasoning.
- [OIF Cyber Intelligence](https://github.com/HuffmanMainNode/OIF-Cyber-Intelligence): defensive indicator normalization.
- [OIF AI Security](https://github.com/HuffmanMainNode/OIF-AI-Security): AI-specific defensive controls.
- [OIF Systems Intelligence](https://github.com/HuffmanMainNode/OIF-Systems-Intelligence): offline host inventory analysis.
- [OIF Collective Intelligence](https://github.com/HuffmanMainNode/OIF-Collective-Intelligence): source-distinct aggregation and dissent.
- [OIF Conformance Lab](https://github.com/HuffmanMainNode/OIF-Conformance-Lab): offline compatibility and fixture checks.

## Versioning and status

The current vocabulary and contract are draft version 0.1.0. Breaking changes require a major version increment once the contract reaches a stable release. Unknown fields should be preserved by consumers where possible. No claim of universal adoption, certification, or exclusive ownership of the general phrase "Open Intelligence" is made.

## Development

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

See [SECURITY.md](SECURITY.md) for trust boundaries. All sample records are illustrative fixtures.
