#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import sys
from datetime import datetime
from typing import Any

from pydantic import BaseModel, EmailStr, ValidationError, constr, validator


class User(BaseModel):
    id: int
    login: constr(min_length=3, max_length=20)
    password: constr(min_length=3, max_length=20)
    email: EmailStr | None
    date: constr(regex=r"\d{4}-\d{2}-\d{2}") | None
    status: int
    is_moderator: bool | None

    @validator("password", pre=True)
    def validate_password(cls, v: True) -> str:
        letters = set(v)
        if not any(map(lambda c: c.isdigit(), letters)):
            raise ValueError("Password does not contain digits")
        elif not any(map(lambda c: c.isupper(), letters)):
            raise ValueError("Password does not contain upper case letters")

        return v

    @validator("date")
    def validate_date(cls, v: str | None) -> datetime | None:
        if v is not None:
            try:
                return datetime.strptime(v, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Incorrect date format, should be YYYY-mm-dd")

        return None

    @validator("status")
    def validate_status(cls, v: int) -> int:
        if v not in (1, 5, 7, 9, 14):
            raise ValueError(f"Incorrect status value {v}")

        return v


def main(command_line: str | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate JSON file")
    parser.add_argument(
        "--json", type=argparse.FileType(mode="r", encoding="utf-8"), required=True
    )

    args = vars(parser.parse_args(command_line))
    users: list[dict[str, Any]] = json.load(args["json"])
    validation_results: list[str] = []

    for user in users:
        try:
            _ = User(**user)
            validation_results.append("OK")
        except ValidationError:
            validation_results.append("Failed")

    print(", ".join(validation_results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
