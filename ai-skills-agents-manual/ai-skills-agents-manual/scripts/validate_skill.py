#!/usr/bin/env python3
"""
validate_skill.py
Teaching script: checks whether a SKILL.md file is well formed.

A skill is just a folder with a SKILL.md file. That file starts with a
"frontmatter" block between two lines of three dashes. The frontmatter must
contain at least a name and a description. This script proves that rule to you
by reading a real file and reporting what it found.

Usage:
    python validate_skill.py hello_skill/SKILL.md

No API key and no internet connection are required. This runs fully offline.
"""

import sys
import os


REQUIRED_FIELDS = ["name", "description"]


def read_frontmatter(path):
    """Return a dict of the frontmatter fields found at the top of the file."""
    with open(path, "r", encoding="utf-8") as handle:
        lines = handle.read().splitlines()

    if not lines or lines[0].strip() != "---":
        raise ValueError("File does not start with a '---' frontmatter line.")

    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    raise ValueError("Frontmatter was opened with '---' but never closed.")


def validate(path):
    print("Checking skill file:", path)
    print("-" * 50)

    if not os.path.exists(path):
        print("RESULT: FAIL. File not found.")
        return False

    try:
        fields = read_frontmatter(path)
    except ValueError as error:
        print("RESULT: FAIL.", error)
        return False

    all_present = True
    for field in REQUIRED_FIELDS:
        if field in fields and fields[field]:
            print("  OK   ", field, "=", fields[field][:60])
        else:
            print("  MISS ", field, "(required, but empty or absent)")
            all_present = False

    for extra in fields:
        if extra not in REQUIRED_FIELDS:
            print("  info ", extra, "=", fields[extra][:60])

    print("-" * 50)
    if all_present:
        print("RESULT: PASS. This is a valid skill definition.")
    else:
        print("RESULT: FAIL. Add the missing required fields above.")
    return all_present


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "hello_skill/SKILL.md"
    ok = validate(target)
    sys.exit(0 if ok else 1)
