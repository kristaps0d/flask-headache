from src import create_app
from flask_scss import Scss

app = create_app()
Scss(app, static_dir='/static/styles', asset_dir='/assets')

if __name__ == '__main__':
    app.run(debug=True)