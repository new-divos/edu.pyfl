#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

import yaml

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some files")

    parser.add_argument(
        "--in", type=argparse.FileType(mode="r", encoding="utf-8"), required=True
    )
    parser.add_argument(
        "--out", type=argparse.FileType(mode="w", encoding="utf-8"), required=True
    )

    args = vars(parser.parse_args())

    data = yaml.safe_load(args["in"])
    if related_hosts := data.get("related_hosts"):
        related_hosts["network"] = dict(
            host="google.com",
            port=8000
        )

    yaml.safe_dump(data, args["out"])
