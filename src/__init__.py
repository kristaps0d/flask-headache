# Library imports
from flask import Flask
from flask_assets import Environment
from dotenv import load_dotenv
from os import getenv

# Submodule imports
from .util.assets import bundles
from .util.database import init_database, deinit_database

# Create a flask instance
app = Flask(__name__)

# Create an app instance
def create_app():

    load_dotenv()
    init_database()

    session = getenv("SESSION_KEY")
    if session is None: 
        raise SystemExit('\nfix(.env)!: missing "SESSION_KEY"\n')

    app.config['SECRET_KEY'] = session

    assets = Environment(app)
    assets.register(bundles)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app

# App teardown deinits database
@app.teardown_appcontext
def teardown_event():
    deinit_database()