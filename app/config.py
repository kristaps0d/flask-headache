# Core packages
import os

# Get root folder path
basedir = os.path.abspath(os.path.dirname(__file__))

# Get enveiromental values
secret_key = os.environ['SECRET_KEY']

if secret_key is None:
	raise SystemExit('Missing "SECRET_KEY" from .env')

# Application configuration
class Configuration():

	SECRET_KEY = secret_key
	SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'
	SQLALCHEMY_TRACK_MODIFICATIONS = False