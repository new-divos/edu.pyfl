#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import hmac
import pickle
import sys
from pathlib import Path
from typing import Final

from faker import Faker
from nanoid import generate


SECRET_KEY: Final[bytes] = generate(size=20).encode("ascii")


def main() -> int:
    out_dir = Path(__file__).parent / "files"
    out_dir.mkdir(parents=True, exist_ok=True)

    fake = Faker("ru_RU")
    person = dict(
        name=fake.name(),
        postcode=fake.postcode(),
        country=fake.country(),
        city=fake.city(),
        address=fake.address(),
        phone_number=fake.phone_number(),
        email=fake.ascii_free_email(),
        company=fake.company(),
        hostname=fake.hostname(),
        job=fake.job(),
    )

    data = pickle.dumps(person)
    digest = hmac.new(SECRET_KEY, data, hashlib.sha256).hexdigest()

    with open(out_dir / "secrets.txt", mode="w", encoding="utf-8") as fs:
        print(SECRET_KEY.decode("ascii"), file=fs)
        print(digest, file=fs)

    with open(out_dir / "file.pickle", mode="wb") as fd:
        fd.write(data)

    return 0


if __name__ == "__main__":
    sys.exit(main())
