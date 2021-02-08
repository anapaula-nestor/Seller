from typing import Type


def validate_type(value: object, type: Type, key: str):
    if not isinstance(value, type) and value is not None:
        raise TypeError(f"{key.capitalize()} must be {type}.")


def validate_not_empty(value: str, key: str):
    if value is None:
        if not value.strip():
            raise ValueError(f"{key.capitalize()} can't be empty.")


def validate_len(value: object, max_len: int, key: str):
    if len(value) > max_len:
        raise ValueError(f"{key.capitalize()} can't be greater than {max_len} characters.")


def validate_be_greater_than_zero(value: float, key: str):
    if value <= 0:
        raise ValueError(f"Value can't be lower than zero.")