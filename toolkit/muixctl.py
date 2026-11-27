#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Offline deployment inventory validation; no deployment side effects."""
import argparse
import json
import sys

def validate(config):
    if not isinstance(config, dict):
        raise ValueError("inventory must be an object")
    if config.get("version") != "0.1":
        raise ValueError("unsupported inventory version")
    profile = config.get("profile")
    if profile not in ("nano", "micro", "regional"):
        raise ValueError("unknown profile")
    if not isinstance(config.get("site"), str) or not config["site"].strip():
        raise ValueError("site identifier required")
    switches = config.get("switches")
    servers = config.get("route_servers")
    for name, items in (("switches", switches), ("route_servers", servers)):
        if not isinstance(items, list):
            raise ValueError(name + " must be a list")
        if any(not isinstance(i, dict) or not isinstance(i.get("id"), str)
               or not i["id"].strip() for i in items):
            raise ValueError(name + " requires nonempty IDs")
        if len({i["id"] for i in items}) != len(items):
            raise ValueError(name + " contains duplicate IDs")
    if len(switches) < (2 if profile == "regional" else 1):
        raise ValueError("insufficient switches")
    domains = set()
    for server in servers:
        domain = server.get("host_failure_domain")
        if not isinstance(domain, str) or not domain.strip():
            raise ValueError("route server host failure domain required")
        domains.add(domain)
    if profile != "nano" and len(domains) < 2:
        raise ValueError("two independent route server host domains required")
    warnings = []
    if len(switches) == 1:
        warnings.append("single switch failure domain")
    if servers and len(domains) < 2:
        warnings.append("route servers lack independent host redundancy")
    return {"site": config["site"], "profile": profile,
            "switches": len(switches), "route_servers": len(servers),
            "warnings": warnings, "conformance_verified": False}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate", "plan"])
    parser.add_argument("inventory")
    args = parser.parse_args()
    try:
        with open(args.inventory, encoding="utf-8") as source:
            result = validate(json.load(source))
        if args.command == "plan":
            result["steps"] = ["verify facility and resources",
                               "validate topology and policy in lab",
                               "prepare isolated management and monitoring",
                               "test recovery and applicable requirements"]
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
