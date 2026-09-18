#!/usr/bin/env python3
"""
skill_runner.py
Teaching script: shows how an agent "invokes" a skill.

When you invoke a skill, the agent does three things:
  1. Loads the SKILL.md instructions.
  2. Checks that you supplied the required inputs (the input contract).
  3. Follows the instructions to produce the output.

This script performs steps 1 and 2 for real, then prints the instruction block
the model would follow for step 3. It runs offline. It does not call a model,
so it will not write the final greeting itself; instead it proves how the
contract is enforced before any generation happens. That check is the part
beginners most often skip, and it is what makes a skill reliable.

Usage:
    python skill_runner.py hello_skill/SKILL.md person_name="Director Wang" occasion="project kickoff"
"""

import sys
import re


def load_skill(path):
    with open(path, "r", encoding="utf-8") as handle:
        content = handle.read()
    return content


def find_required_inputs(content):
    """Read the Inputs section and return input names marked (required)."""
    required = []
    for line in content.splitlines():
        match = re.match(r"\s*-\s*([a-zA-Z_]+)\s*\(required\)", line)
        if match:
            required.append(match.group(1))
    return required


def parse_user_inputs(pairs):
    supplied = {}
    for pair in pairs:
        if "=" in pair:
            key, value = pair.split("=", 1)
            supplied[key.strip()] = value.strip().strip('"')
    return supplied


def main():
    if len(sys.argv) < 2:
        print('Usage: python skill_runner.py PATH/SKILL.md key="value" ...')
        sys.exit(1)

    path = sys.argv[1]
    supplied = parse_user_inputs(sys.argv[2:])

    content = load_skill(path)
    required = find_required_inputs(content)

    print("Loaded skill:", path)
    print("Required inputs declared by the skill:", required or "none")
    print("Inputs you supplied:", supplied or "none")
    print("-" * 55)

    missing = [name for name in required if name not in supplied]
    if missing:
        print("CONTRACT CHECK: FAIL. Missing required inputs:", missing)
        print("The agent should stop and ask you for these before generating.")
        sys.exit(1)

    print("CONTRACT CHECK: PASS. All required inputs are present.")
    print("-" * 55)
    print("The agent would now follow these instructions to generate output:\n")
    in_process = False
    for line in content.splitlines():
        if line.strip().lower().startswith("## process"):
            in_process = True
            continue
        if in_process and line.startswith("## "):
            break
        if in_process and line.strip():
            print("   ", line)


if __name__ == "__main__":
    main()
