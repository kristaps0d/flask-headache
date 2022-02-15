# Flask modules
from flask import render_template, request

# App modules
from app import app

# App main route
@app.route('/', defaults={'path': 'index.html'})

# Default site route
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/u/<path>')
def my(path):
	try:
		return render_template(f'u/{path}.html')
	except:
		return render_template('page-404.html')

@app.route('/public/<path>')
def room(path):
	try:
		return render_template(f'public/{path}.html')
	except:
		return render_template('page-404.html')

# Missing page handler
@app.errorhandler(404)
def not_found(event):
	return render_template('page-404.html')