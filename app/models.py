# App modules
from app import db

class Sessions(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(24), unique=False, nullable=False)
	room = db.Column(db.String(24), unique=True, nullable=False)
	passw = db.Column(db.String(24), unique=False, nullable=True)

	def __init__(self):
		self.id = id
		self.title = title
		self.room = room
		self.passw = passw

	def save(self):
		# Save and commit session
		db.session.add(self)
		db.session.commit()
		return self

try:
	# Query database
	Sessions.Query.all()
except:
	# Initiate database
	db.create_all()
