import os
class AppConfig(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
	#SECRET_KEY = os.urandom(64)		
	#'sqlite:///data.db'