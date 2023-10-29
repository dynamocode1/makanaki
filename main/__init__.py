from flask import Flask,g,request,make_response,session,url_for,redirect,render_template
from flask_login import LoginManager
from config import AppConfig
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import time

#from .models import Posts
db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'



login_manager = LoginManager()
from .main import main_bp
from .auth import auth_bp
from .admin import admin_bp
def create_app():
	app.config.from_object(AppConfig)
	#sessions = Session(app)
	bcypt = Bcrypt(app)
	db.init_app(app)
	app.register_blueprint(main_bp,url_prefix = '/main')
	login_manager.init_app(app)
	app.register_blueprint(auth_bp,url_prefix = '/auth')
	app.register_blueprint(admin_bp,url_prefix = '/admin')

	login_manager.login_view = 'auth.register'
	@app.route('/')
	def index():
		return redirect(url_for('main.home'))
	
	return app
