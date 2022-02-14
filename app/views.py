# Flask modules
from flask import render_template, request

# App modules
from app import app

# App main route
@app.route('/', defaults={'path': 'index.html'})

# Default site route
@app.route('/<path>')
def index(path):
	return render_template('index.html')
	#return render_template('voting.html')