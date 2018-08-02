from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login



class User(UserMixin, db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __init__(self, username, email, password_hash):
		self.username = username
		self.email = email
		self.password_hash = password_hash

	def set_password(password):
		password_hash = generate_password_hash(password)
		return password_hash

	def check_password(password, password_hash):
		return check_password_hash(password_hash, password)


	def __repr__(self):
		return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))