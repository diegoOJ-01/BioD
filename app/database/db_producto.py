from pymysql import connect
from os import getenv
from os.path import abspath
from dotenv import load_dotenv

load_dotenv(abspath('.env'))


def conexion():
    return connect(
        host=getenv('MYSQL_HOST'),
        database=getenv('MYSQL_DB'),
        user=getenv("MYSQL_USER"),
        password=getenv('MYSQL_PASSWORD')
    )
