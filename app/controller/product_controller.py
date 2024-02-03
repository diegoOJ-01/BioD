from app.database import db_producto

from app.models.Producto import Producto
from app.models.exceptions import InvalidObject

from app.helpers.upper_field import upper_dataclass_fields


def get_products(sorted: bool = False) -> list[Producto]:
    """Fetchs all the rows in the table.

    Args:
        sorted (bool): fetch the rows sorted.

    Returns:
        list[Producto]: all the rows fetched in a list of products.
    """

    return db_producto.read_products(sorted)


def insert_product(producto: Producto) -> Producto:
    """Saves a new record.

    Args:
        producto: Producto. The product to be recorded.

    Returns:
        Producto: A product with assigned id.
    """

    validate_product(producto)

    if not all([producto.id_almacen, producto.cod_barra, producto.precio]):
        raise InvalidObject(
            "the product has no all the parameters: bar code, store id and price."
        )

    return db_producto.create_product(
        upper_dataclass_fields(producto)
    )


def update_product(producto: Producto) -> Producto:
    """updates a record in the database.

    Args:
        producto (Producto): the product with new values and same cod_barra.

    Returns:
        Producto: the product with updated fields.
    """

    validate_product(producto)

    return db_producto.update_product(
        upper_dataclass_fields(producto)
    )


def delete_product(producto: Producto) -> Producto:
    """deletes a record in the database.

    Args:
        producto (Producto): the product with new values and same cod_barra.

    Returns:
        Producto: the product with updated fields.
    """
    validate_product(producto)

    return db_producto.delete_product(producto)


def fetch_one_product(producto: Producto) -> Producto:
    """Fetchs a product in the database.

    Args:
        producto (Producto): the product to be fetched.

    Returns:
        Producto | None: the product fetched, else None.
    """

    validate_product(producto)
    return upper_dataclass_fields(
        db_producto.fetch_one_product(producto)
    )


def validate_product(producto: Producto):
    if not isinstance(producto, Producto):
        raise InvalidObject(
            f"Product was expected, but {type(producto).__name__} was given."
        )
