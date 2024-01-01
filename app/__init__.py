from flask import Flask
from config import Config
from .routes import Home


app = Flask(__name__, template_folder=Config.TEMPLATE_FOLDER, static_folder=Config.STATIC_FOLDER)
app.config.from_object(Config)

app.register_blueprint(Home, url_prefix='/')
