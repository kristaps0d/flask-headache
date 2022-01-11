from flask import Flask
from flask_assets import Environment
from .util.assets import bundles

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dfghdrfhfh'

    assets = Environment(app)
    assets.register(bundles)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app