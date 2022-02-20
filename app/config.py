# Core packages
import os, dotenv
from secrets import token_urlsafe

# Get root folder path
basedir = os.path.abspath(os.path.dirname(__file__))

# Get enveiromental values
dotenv.load_dotenv()

secret_key = os.getenv('SECRET_KEY')
if secret_key is None:
	print('\n	Missing "SECRET_KEY" from .ENV')
	print('	[Auto generated key]: ' + token_urlsafe(16))

database_uri = os.getenv('DATABASE_URI')
if database_uri is None:
	print('\n	Missing "DATABASE_URI" from .ENV')
	print('	[EXAMPLE]: sqlite:///database.sqlite3\n')

if not secret_key or not database_uri:
	raise SystemExit()

# Application configuration
class Configuration():

	SECRET_KEY = secret_key
	SESSION_COOKIE_NAME = "session"
	SESSION_COOKIE_HTTPONLY = True

	STATIC_FOLDER = 'static'
	TEMPLATE_FOLDER = 'templates'

	SQLALCHEMY_DATABASE_URI = database_uri
	SQLALCHEMY_TRACK_MODIFICATIONS = False
