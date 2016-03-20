import subprocess
from flask.ext.script import Manager
from tracking import app, db
from tracking.user.model import User

manager = Manager(app)

@manager.command
def createdb():
  """Create DB tables"""
  db.create_all()
  
@manager.command
def initdb():
  """Init/reset database."""
  db.drop_all()
  db.create_all()
  user = User("phillipwei@gmail.com", "le0nard0", "Phillip", "Wei")
  db.session.add(user)
  db.session.commit()

@manager.command
def runcelery():
  """Start celery server."""
  subprocess.call("celery -a tracking worker --config=config --loglevel=info --autoreload", shell=True)

@manager.command
def clean():
  """Removes old pyc and css generated files."""
  import os
  import fnmatch
  for root,dirs,files in os.walk('.'):
    for file in fnmatch.filter(files, '*.pyc'):
      os.remove(os.path.join(root,file))
      print('removing ' + os.path.join(root,file))

@manager.command
def public():
  app.run(host='0.0.0.0',threaded=True)

if __name__ == "__main__":
  manager.run()
