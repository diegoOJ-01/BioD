from typing import Optional
import connection

from dataclasses import astuple, fields, replace

from app.models.Producto import Producto
from app.models.exceptions import ObjectNotFound, ObjectAlreadyExists


def create_product(producto: Producto) -> Producto:
    """Saves a new record.

    Args:
        producto: Producto. The product to be recorded.

    Returns:
        Producto: the new product with assigned id.
    """

    if product_exists(producto):
        raise ObjectAlreadyExists(
            f"The product with bar code {producto.cod_barra} already exists."
        )

    # ignore the id and unique columns.
    product_fields = fields(producto)[2:]

    query = "INSERT INTO Productos"
    query += f"({",".join([field.name for field in product_fields])}) "
    query += f"VALUES({",".join(["%s"] * len(product_fields))})"

    new_id = connection.fetch_lastrow_id(
        query,
        astuple(producto)[2:]
    )

    return replace(producto, id_=new_id)


def read_products(sorted: bool = False) -> list[Producto]:
    """Fetch all the rows in the table.

    Args:
        sorted (bool): fetch the rows sorted.

    Returns:
        list[Producto]: all the rows fetched in a list of products.
    """
    query = "SELECT * FROM Productos"

    # prevent any value that is not a bool.
    if sorted == True:
        query += " ORDER BY id_"

    records: tuple[dict] = connection.fetch_all(query)

    return [Producto(**record) for record in records]


def update_product(producto: Producto) -> Producto:
    """updates a record in the database.

    Args:
        producto (Producto): the product with new values and same cod_barra.

    Returns:
        Producto: the same product.
    """

    if not product_exists(producto):
        raise ObjectNotFound(
            f"No product with bar code {producto.cod_barra}."
        )

    product_fields = fields(producto)[2:]

    query = "UPDATE Productos SET "
    query += ",".join([f"{product_field.name} = %s" for product_field in product_fields])
    query += " WHERE cod_barra = %s"

    connection.fetch_none(
        query,
        astuple(producto)[2:] + (producto.cod_barra,)
    )

    return producto


def delete_product(producto: Producto) -> Producto:
    """delete a record in the database.

    Args:
        product (Producto): the product to be deleted

    Returns:
        bool: true if deleted, otherwhise false.
    """

    if not product_exists(producto):
        raise ObjectNotFound(
            f"No product with bar code {producto.cod_barra}."
        )

    query = "DELETE * FROM Productos WHERE cod_barra = %s"
    connection.fetch_none(
        query,
        (producto.cod_barra,)
    )

    return producto


def fetch_one_product(producto: Producto) -> Optional[Producto]:
    """Fetch a product in the database.

    Args:
        producto (Producto): the product to be fetched.

    Returns:
        Producto | None: the product fetched, else None.
    """
    query = "SELECT * FROM Productos WHERE cod_barra = %s"
    record = connection.fetch_one(query, producto.cod_barra)

    if record is None:
        raise ObjectNotFound(
            f"No product with bar code {producto.cod_barra}."
        )

    return replace(producto, **record)


def product_exists(producto: Producto) -> bool:
    """checks if a product exists in the database.

    Args:
        producto (Producto): Product to search.

    Returns:
        bool: True if exists, otherwhise False.
    """
    query = "SELECT * FROM Productos WHERE cod_barra = %s"
    return connection.record_exists(query, producto.cod_barra)
