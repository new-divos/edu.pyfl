#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import tomllib


if __name__ == "__main__":
    # The argparse module is being used to parse command-line arguments passed
    # to this Python script.
    parser = argparse.ArgumentParser(description="Process some files")
    # --toml argument is expecting a file to be passed as input, which is 
    # specified using type=argparse.FileType(mode="rb"). Here, mode="rb" 
    # means the file is opened in binary read mode. This is useful when 
    # working with binary files.
    parser.add_argument(
        "--toml", type=argparse.FileType(mode="rb"), required=True
    )
    # --json argument is expecting a file to be passed as output, which 
    # is specified using type=argparse.FileType(mode="w", encoding="utf-8"). 
    # Here, mode="w" means the file is opened in write mode and 
    # encoding="utf-8" specifies the file encoding.
    parser.add_argument(
        "--json", type=argparse.FileType(mode="w", encoding="utf-8"), required=True
    )
    # Both the --toml and --json arguments are required to be passed while 
    # running the script, which is enforced using required=True.

    # The vars() function is used to convert the Namespace object returned 
    # by parse_args() into a dictionary object. This allows easy access to 
    # the parsed arguments in the code.
    args = vars(parser.parse_args())

    # A dictionary object parsed is created to store the data parsed from the 
    # TOML file.
    parsed = dict()
    # The tomllib module is used to load the data from the TOML file specified 
    # by the --toml command-line argument.
    data = tomllib.load(args["toml"])
    # If the "tool" or "poetry" keys are missing from the TOML file, no data 
    # is added to the parsed dictionary, so the resulting JSON file will only 
    # contain keys that have been populated.
    if tool := data.get("tool"):
        if poetry := tool.get("poetry"):
            parsed["version"] = poetry.get("version")
            parsed["name"] = poetry.get("name")
            parsed["authors"] = poetry.get("authors")

    # The json module is used to write the contents of the parsed dictionary 
    # to a JSON file specified by the --json command-line argument using 
    # the dump() method.
    json.dump(parsed, args["json"], indent=3)


