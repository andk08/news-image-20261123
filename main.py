#!/usr/bin/env python3
"""Entry program for news-image-20261123.

Copies the pre-rendered entry.png shipped in this repository to the
output directory. Standard library only, no network, deterministic:
every run writes the same bytes.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    # The grader sets MAKEFUN_OUTPUT_DIR; /output is the documented default.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    os.chmod(dest, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
