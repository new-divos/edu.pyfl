#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import hmac
import json
import pickle
import sys
from pathlib import Path


def main() -> int:
    out_dir = Path(__file__).parent / "files"
    with open(out_dir / "secrets.txt", mode="r", encoding="utf-8") as fs:
        secret_key_str, digest, *_ = [s.strip() for s in fs.readlines()]

    with open(out_dir / "file.pickle", mode="br") as fd:
        data = fd.read()

    secret_key = secret_key_str.encode("ascii")
    expected_digest = hmac.new(secret_key, data, hashlib.sha256).hexdigest()
    code = 0
    if expected_digest != digest:
        print("Data integrity violated", file=sys.stderr)
        answer = dict(answer="not correct")
        code = 1
    else:
        answer = pickle.loads(data)
        if isinstance(answer, dict):
            answer["answer"] = "easy pickle"

    with open(out_dir / "answer.json", mode="w", encoding="utf-8") as fj:
        json.dump(answer, fj, ensure_ascii=False, indent=4)

    return code


if __name__ == "__main__":
    sys.exit(main())
