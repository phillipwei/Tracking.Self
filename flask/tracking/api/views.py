from datetime import datetime
from dateutil import parser
from dateutil import tz
from os import listdir, makedirs, path
from flask import Blueprint, abort, jsonify, request, send_file
from flask.ext.login import login_required
from werkzeug import secure_filename

from .. import app, db
from ..user.model import User
from .model import Activity, Weight

api = Blueprint('api', __name__, url_prefix='/api')

#@app.before_request
#def log():
#  app.logger.debug(request.headers)
#  app.logger.debug(request.form)
#  app.logger.debug(request.files)

@api.route('/upload', methods=['POST'])
def upload():
  # Check Authorization
  auth = request.authorization
  user = User.authorize(auth.username, auth.password) if auth else None
  if user is None:
    abort(401)
  # Save the file; process the file
  file = request.files['file']
  if file:
    timestamp = parser.parse(request.values['datetime'])
    filename = secure_filename(file.filename)
    dir = app.config['UPLOAD_FOLDER']
    if not path.exists(dir):
      makedirs(dir)
    filepath = path.join(dir, filename)
    file.save(filepath)
    activity = Activity(timestamp, filepath)
    db.session.add(activity)
    db.session.commit()
  return ''

@api.route('/weight', methods=['POST'])
def add_weight():
  timestamp = request.form.get('datetime')
  if timestamp:
    timestamp = parser.parse(timestamp)
  else:
    timestamp = datetime.now()
  if timestamp.tzinfo is None:
    timestamp = timestamp.replace(tzinfo=tz.tzlocal())
  qty = request.form['qty']
  unit = request.form.get('unit') or 'lb'
  weight = Weight(timestamp, qty, unit)
  db.session.add(weight)
  db.session.commit()
  return ''
  
@api.route('/weight', methods=['GET'])
@login_required
def get_weight():
  start = request.args.get('start')
  if start is not None:
    start = parser.parse(request.args.get('start'))
    if start.tzinfo is None:
      start = start.replace(tzinfo=tz.tzlocal())
    
  end = request.args.get('end')
  if end is not None:
    end = parser.parse(request.args.get('end'))
    if end.tzinfo is None:
      end = end.replace(tzinfo=tz.tzlocal())
  
  return jsonify(weight=[i.serialize for i in Weight.find(start, end)])
  
@api.route('/query')
@login_required
def query():
  # todo: none handling
  start = parser.parse(request.args.get('start'))
  end = parser.parse(request.args.get('end'))
  if start.tzinfo is None:
    start = start.replace(tzinfo=tz.tzlocal())
  if end.tzinfo is None:
    end = end.replace(tzinfo=tz.tzlocal())
  return jsonify(activities=[i.serialize for i in Activity.find(start, end)])
  '''
  dir = app.config['UPLOAD_FOLDER']
  files = [ f for f in listdir(dir) if path.isfile(path.join(dir,f)) ]
  return jsonify({'car' : files})
  '''
  
# http://stackoverflow.com/questions/13706382/how-to-get-static-files-in-flask-without-url-forstatic-file-name-xxx
@api.route('/img/<filename>')
@login_required
def img(filename):
  if '..' in filename or '/' in filename:
    abort(404)
  dir = app.config['UPLOAD_FOLDER']
  return send_file('../' + dir + '/' + filename, mimetype="image/png")

