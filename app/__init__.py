# Flask modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initiate a flask instance
# and load configuration
app = Flask(__name__)
app.config.from_object('app.config.Configuration')

# Initiate a db instance
db = SQLAlchemy(app)

from app import views, models