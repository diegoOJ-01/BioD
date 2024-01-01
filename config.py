from os import getenv
from os.path import abspath
from dotenv import load_dotenv

load_dotenv(abspath(".env"))


class Config:
    DEBUG = True

    TEMPLATE_FOLDER = 'views/templates/'
    STATIC_FOLDER = 'views/static/'

    MYSQL_DB = getenv("MYSQL_DB")
    MYSQL_HOST = getenv("MYSQL_HOST")
    MYSQL_USER = getenv("MYSQL_USER")
    MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
