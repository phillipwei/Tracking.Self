from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required

from .model import User

class LoginForm(Form):
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Login')