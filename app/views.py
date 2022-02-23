# Flask modules
from flask import render_template, request, g, session

# App modules
from app import app, models

# App main route
@app.route('/', defaults={'path': 'index.html'})

# Default site route
@app.route('/')
def index():
	return render_template('index.html', wrong=False)

@app.route('/session/<string:route>', methods=['post', 'get'])
def Session(route):
	row = models.Sessions.query.filter_by(room=route).first()
	if row is None: return "", 404
	
	if request.method == "POST":
		pass
	else:
		return render_template('/view.html', room=route, expiry="2h 24m 12s")

@app.route('/session/reserve/<route>')
def Reserve(route):
	row = models.Sessions.query.filter_by(room=route).first()
	if row is None: return "", 404
	return "", 200

@app.route('/session/create', methods=['get', 'post'])
def Create():
	if request.method == 'POST':
		
		req = request.form

		room = req['room']
		title = req['title']
		password = req['password']
		tokens = req['tokens']

		try:
			session = models.Sessions(room=room, title=title, password=password)
			session.tokens(int(tokens)).save()
		except:
			return '', 400

		return '', 200
	else:
		return render_template('create.html')

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