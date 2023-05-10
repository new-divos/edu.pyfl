#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

from pydantic import (
    BaseModel, 
    EmailStr, 
    ValidationError, 
    constr,
    parse_obj_as, 
    validator
)


class User(BaseModel):
    id: int
    login: constr(min_length=3, max_length=20)
    password: constr(min_length=3, max_length=50)
    email: EmailStr | None
    date: date | None
    status: int
    is_moderator: bool | None

    @validator("password")
    def validate_password_must_contain_digit(cls, v: str) -> str:
        if not any([c.isdigit() for c in v]):
            raise ValueError("Password does not contain digits")
        
        return v
    
    @validator("password")
    def validate_password_must_contain_upper_case(cls, v: str) -> str:
        if not any([c.isupper() for c in v]):
            raise ValueError("Password does not contain upper case letters")

        return v

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
            _ = parse_obj_as(User, user)
            validation_results.append("OK")
        except ValidationError:
            validation_results.append("Failed")

    log_path = Path(__file__).parent / "log"
    log_path.mkdir(parents=True, exist_ok=True)

    with open(log_path / "main.log", mode="w", encoding="utf-8") as flog:
        for idx, row in enumerate(validation_results, 1):
            print(f"{idx}: {row}", file=flog)

    print(",".join(validation_results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
