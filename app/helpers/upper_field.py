from dataclasses import dataclass, is_dataclass, replace, fields
from typing import Type

from app.models.Exceptions import InvalidDataClassException


def upper_dataclass_fields(dataclass: Type[dataclass]) -> Type[dataclass]:
    """
    returns a new dataclass with uppercased fields.

    Returns:
        Type[dataclass]: new dataclass with uppercased fields.
    """
    if not is_dataclass(dataclass):
        raise InvalidDataClassException(
            "the given argument must be a dataclass."
        )

    dataclass_fields = fields(dataclass)

    changes = {}
    for field in dataclass_fields:
        field_name = field.name
        field_value = getattr(dataclass, field_name)

        if isinstance(field_value, str):
            field_value = field_value.upper()

        changes[field_name] = field_value

    return replace(dataclass, **changes)


def upper_field(field: str) -> str:
    """
    convert a field into uppercase.

    Args:
        field (str): the field to be converted

    Returns:
        str: the field in uppercase
    """
    return str(field).upper()
