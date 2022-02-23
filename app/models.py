# Flask modules
from sqlalchemy_mutable import MutableList
from sqlalchemy import PickleType

# App modules
from app import db

# Core packages
from datetime import datetime
from secrets import token_urlsafe

class Sessions(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	room = db.Column(db.String(6), unique=True, nullable=False)
	title = db.Column(db.String(24), unique=False, nullable=False)
	password = db.Column(db.String(24), unique=False, nullable=True)
	tokens = db.Column(MutableList.as_mutable(PickleType), default=[])
	expiry = db.Column(db.DateTime, default=datetime.now)

	def __init__(self, room, title, password):
		self.room = room
		self.title = title
		self.password = password

	def tokens(self, invites, expire=False):

		tokens = []
		for token in range(invites):
			tokens.append(token_urlsafe(24))

		self.tokens = tokens
		self.save()

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
