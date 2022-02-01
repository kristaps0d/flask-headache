# Core packages
import os
import dotenv

# Get root folder path
basedir = os.path.abspath(os.path.dirname(__file__))

# Get enveiromental values
dotenv.load_dotenv()
secret_key = os.getenv("SECRET_KEY")

if secret_key is None:
	raise SystemExit('Missing "SECRET_KEY" from .env')

# Application configuration
class Configuration():

	SECRET_KEY = secret_key
	SQLALCHEMY_DATABASE_URI = 'sqlite:///static/database.sqlite3'
	SQLALCHEMY_TRACK_MODIFICATIONS = False