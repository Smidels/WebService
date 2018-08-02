import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'postgresql+psycopg2://smidels:7895@localhost/aaa'
	SQLALCHEMY_TRACK_MODIFICATIONS = False