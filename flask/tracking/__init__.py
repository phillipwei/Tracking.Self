from flask import Flask, redirect, url_for

app = Flask(__name__)
app.config.from_object('config')

# Extensions
from celery import Celery
from flask.ext.babel import Babel
from flask.ext.login import LoginManager
from flask.ext.mail import Mail 
from flask.ext.sqlalchemy import SQLAlchemy
babel = Babel(app)
celery = Celery()
celery.config_from_object(app.config)
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message = None
login_manager.setup_app(app)
mail = Mail(app)
db = SQLAlchemy(app)

# Blueprints
from .webapp import webapp
from .user import user
from .api import api
for bp in [webapp, user, api]:
  app.register_blueprint(bp)

@app.route('/')
def index():
  return redirect(url_for('webapp.entry'))
