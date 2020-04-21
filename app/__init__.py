from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config) # linking config file to our app
db = SQLAlchemy(app) # represents database
migrate = Migrate(app, db) # represents migration engine

from app import routes, models