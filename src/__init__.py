from flask import Flask

def create_app():
    
    app = Flask(__name__)
    # DOT ENV
    app.config['SECRET_KEY'] = 'dfghdrfhfh'

    from .views import views
    app.register_blueprint(views, url_prefix='/')


    return app