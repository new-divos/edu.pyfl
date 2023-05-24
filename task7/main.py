#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mimetypes
import sys
import uuid
from pathlib import Path
from typing import Final

import requests


URL_IN: Final[str] = "https://httpbin.org/image/jpeg"
URL_OUT: Final[str] = "https://httpbin.org/post"


def main() -> int:
    file_path = Path(__file__).parent.joinpath("files", f"{uuid.uuid4()}.jpeg")

    with requests.get(URL_IN, stream=True) as r, open(file_path, "wb") as fout:
        for chunk in r.iter_content(chunk_size=4096):
            if chunk:
                fout.write(chunk)

    with open(file_path, "rb") as fin:
        content = fin.read()

    files = {
        "file": (
            file_path.name,
            content,
            mimetypes.guess_type(file_path.name),
            {"Expires": "0"},
        )
    }
    r = requests.post(URL_OUT, files=files)
    print(r.text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
