from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.ext.login import current_user, logout_user, login_user
from flask.ext.mail import Message

from .. import app, db, login_manager
from ..tasks import send_mail
from .model import User
from .forms import LoginForm

user = Blueprint('user', __name__, url_prefix='/user')

@login_manager.user_loader
def load_user(id):
  try:
    return User.query.get(int(id))
  except:
    return None
    
@user.route('/login', methods = ['GET', 'POST'])
def login():
  if current_user.is_authenticated():
    return redirect(url_for('webapp.entry'))
  login_form  = LoginForm()
  if login_form.validate_on_submit():
    user = User.find("phillipwei@gmail.com")
    print(login_form.password.data)
    if user and user.check_password(login_form.password.data):
      login_user(user, remember=True)
      return redirect(request.args.get('next') or url_for('webapp.entry'))
    flash('Wrong email or password')
  return render_template('user/login.html', page_title='Login', login=login_form)

@user.route('/logout', methods = ['GET', 'POST'])
def logout():
  if not current_user.is_authenticated():
    pass
  else:
    logout_user()
  return redirect(url_for('webapp.entry'))
