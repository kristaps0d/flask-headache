# App modules
from app import db

class Rooms(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	key = db.Column(db.String(24), unique=True, nullable=False)
	password = db.Column(db.String(24), unique=False, nullable=True)

try:
	# Query database
	Rooms.Query.all()
except:
	# Initiate database
	db.create_all()