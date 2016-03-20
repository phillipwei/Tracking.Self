import string
from datetime import datetime
from random import choice
from werkzeug.security import generate_password_hash, check_password_hash

from .. import app
from .. import db

from .constants import ADMIN, USER, ACTIVE, INACTIVE

class User(db.Model):
    __tablename__ = 'users'
    
    id         = db.Column(db.Integer, primary_key=True)
    role_id    = db.Column(db.SmallInteger, default=USER)
    status_id  = db.Column(db.SmallInteger, default=ACTIVE)
    email      = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(120))
    last_name  = db.Column(db.String(120))
    # Note: Format of generate_password_hash is method$salt$hash
    #       default method=sha1, default salt length=8
    #       sha1 digest size is 160 bits; hex representation requires 40 bytes
    #       4 + 1 + 8 + 1 + 40 = 54
    pw_hash           = db.Column(db.String(54))
    
    def __init__(self, email=None, password=None, first_name=None, last_name=None):
        self.email = email
        self.set_password(password)
        self.first_name = first_name;
        self.last_name = last_name;
        
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    
    def is_admin(self):
        return self.role_id == ADMIN

    def is_active(self):
        return self.status_id != INACTIVE

    def __repr__(self):
        return '<User %s>' % (self.email)
        
    @staticmethod
    def authorize(email, password):
        user = User.query.filter_by(email=email.lower()).first()
        if user and user.check_password(password):
            return user
        return None
    
    @staticmethod
    def find(email):
        user = User.query.filter_by(email=email).first()
        return user if user else None