#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import sys


def main(command_line: str | None = None) -> int:
    parser = argparse.ArgumentParser(description="Reformat JSON file")
    parser.add_argument(
        "--in", type=argparse.FileType(mode="r", encoding="utf-8"), required=True
    )
    parser.add_argument(
        "--out", type=argparse.FileType(mode="w", encoding="utf-8"), required=True
    )

    args = vars(parser.parse_args(command_line))

    data = json.load(args["in"])
    json.dump(data, args["out"], ensure_ascii=False, indent=4)

    return 0


if __name__ == "__main__":
    sys.exit(main())
