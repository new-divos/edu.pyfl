#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from typing import Final

from faker import Faker
from nanoid import generate


SECRET_KEY: Final[str] = generate(size=20)


def main(command_line: str | None = None) -> int:
    out_dir = Path(__file__).parent / "files"
    out_dir.mkdir(parents=True, exist_ok=True)

    fake = Faker("ru_RU")
    user = dict(
        name=fake.name(),
        login=fake.login()
    )

    # with open(out_dir / "")

    return 0


if __name__ == "__main__":
    sys.exit(main())
