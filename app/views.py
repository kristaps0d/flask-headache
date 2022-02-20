# Flask modules
from flask import render_template, redirect, request, g, session

# App modules
from app import app, models

# from app import dev_views	# FOR DEVELOPMENTAL PURPUSES, PURGE AFTER

# App main route
@app.route('/', defaults={'path': 'index.html'})

# Default site route
@app.route('/')
def index():
	return render_template('index.html', wrong=False)

@app.route('/u/<path>')
def my(path):
	try:
		return render_template(f'u/{path}.html')
	except:
		return render_template('page-404.html')

@app.route('/session/<path>')
def room(path):
	try:
		return '<h1>HELOS</h1>'
	except:
		return render_template('page-404.html')

@app.route('/session/reserve/<room>')
def session(room):

	data = models.Sessions.query.filter_by(room=room).first()
	if data is None:
		return "", 404

	return "", 200

# Missing page handler
@app.errorhandler(404)
def not_found(event):
	return render_template('page-404.html'), 404