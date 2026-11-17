"""Offline validation for Open Intelligence resource manifests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = ("id", "name", "resource_type", "publisher", "version", "capabilities")


def validate_resource(resource: Any) -> list[str]:
    """Return validation errors for a resource manifest; an empty list means valid."""
    if not isinstance(resource, dict):
        return ["resource must be a JSON object"]

    errors = [f"missing required field: {field}" for field in REQUIRED_FIELDS if field not in resource]
    if errors:
        return errors

    for field in ("id", "name", "resource_type", "version"):
        if not isinstance(resource[field], str) or not resource[field].strip():
            errors.append(f"{field} must be a non-empty string")

    publisher = resource["publisher"]
    if not isinstance(publisher, dict) or not isinstance(publisher.get("name"), str) or not publisher["name"].strip():
        errors.append("publisher.name must be a non-empty string")

    capabilities = resource["capabilities"]
    if not isinstance(capabilities, list) or not capabilities:
        errors.append("capabilities must be a non-empty array")
    else:
        for index, capability in enumerate(capabilities):
            if not isinstance(capability, dict) or not isinstance(capability.get("id"), str):
                errors.append(f"capabilities[{index}] must be an object with a string id")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an OI resource manifest.")
    parser.add_argument("manifest", type=Path, help="Path to a JSON manifest")
    args = parser.parse_args()

    try:
        resource = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    errors = validate_resource(resource)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"VALID: {args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
