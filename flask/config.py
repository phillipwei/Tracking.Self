import os

_basedir=os.path.abspath(os.path.dirname(__file__))

# Flask Config
DEBUG=True
TESTING=False
SECRET_KEY='pleasegoawayNSA'
#SERVER_NAME = 'www.pokercheckup.com'

# SQLAlchemy
SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS={}

# Celery
BROKER_URL='amqp://guest@localhost//'
CELERY_IMPORTS=('tracking', )

# WTForms
CSRF_ENABLED=True
CSRF_SESSION_KEY='shooshoodontlook'

# Mail
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USERNAME='phillipweitracking@gmail.com'
MAIL_PASSWORD='zIH8Jq9twu0Kn40h3R9s'
MAIL_DEFAULT_SENDER='Tracking <phillipweitracking@gmail.com>'

# Tracking
UPLOAD_FOLDER='uploads'
PUBLIC_URL_ROOT = 'http://localhost:5000/tracking'