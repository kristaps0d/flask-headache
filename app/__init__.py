# Flask modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initiate a flask instance
app = Flask(__name__)
app.config.from_object('app.config.Configuration')

# Initiate a db instance
db = SQLAlchemy(app)

# Initiate submodules with app context
with app.app_context():
	from app import views, models, assets