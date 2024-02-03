import pymysql as mysql
from pymysql.cursors import DictCursor

from contextlib import contextmanager
from typing import Any, Generator

from os import getenv
from os.path import abspath
from dotenv import load_dotenv

load_dotenv(abspath('.env'))


def fetch_all(query: str) -> tuple[dict[str, Any], ...]:
    """
    Fetch all the rows in a table.

    Args:
        query (str): Query to execute.

    Returns:
        tuple[dict[str, Any], ...]: all the rows fetched in a tuple of dicts.
    """

    with __get_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def fetch_one(query: str, identifier: Any) -> dict[str, Any] | None:
    """
    Fetch the next row in a table.

    Args:
        query (str): Query to execute.
        identifier (Any): Identifier by which the record will be matched.

    Returns:
        dict: matched record.
    """

    with __get_cursor() as cursor:
        cursor.execute(
            query,
            (identifier,)
        )

        return cursor.fetchone()


def fetch_none(query: str, args=None) -> None:
    """executes a query.

    Args:
        query (str): Query to execute.
        args (tuple, list or dict): Parameters used with query. (optional).
    """

    with __get_cursor() as cursor:
        cursor.execute(query, args)


def fetch_lastrow_id(query: str, args=None) -> int:
    """
    returns the value generated for an AUTO_INCREMENT column
    by the last INSERT or UPDATE statement executed.

    Args:
        query (str): Query to execute.
        args (tuple, list or dict): Parameters used with query. (optional).

    If args is a list or tuple, %s can be used as a placeholder in the query.\n
    If args is a dict, %(name)s can be used as a placeholder in the query.

    Returns:
        int: the value generated.
    """
    with __get_cursor() as cursor:
        cursor.execute(query, args)

        return cursor.lastrowid


def record_exists(query: str, identifier: Any) -> bool:
    """checks if a record exists in the database.

    Args:
        query (str): Query to execute.
        identifier (Any): Id in which the record will be searched.

    Returns:
        bool: True if exists, otherwhise false.
    """
    return True if fetch_one(query, identifier) else False


@contextmanager
def __get_cursor() -> Generator[DictCursor, None, None]:
    """
    Establish a connection to the MySQL database.
    and 
    create a new cursor to execute queries with.

    Returns:
        DictCursor: the new cursor.

    Yields:
        Generator[DictCursor]: generate cursors an it's converted to a context manager.
    """
    connection: mysql.Connection = __get_connection()
    cursor: DictCursor = connection.cursor(DictCursor())

    try:
        yield cursor
        connection.commit()

    finally:
        cursor.close()
        connection.close()


def __get_connection() -> mysql.Connection:
    return mysql.connect(
        host=getenv('MYSQL_HOST'),
        database=getenv('MYSQL_DB'),
        user=getenv("MYSQL_USER"),
        password=getenv('MYSQL_PASSWORD')
    )
