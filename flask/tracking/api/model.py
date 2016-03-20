import string, json
from datetime import datetime
from dateutil import tz

from .. import app
from .. import db
  
class Activity(db.Model):
  __tablename__ = 'activity'
  
  id         = db.Column(db.Integer, primary_key=True)
  datetime   = db.Column(db.DateTime(timezone=True))
  image_path = db.Column(db.String(120))
  
  def __init__(self, datetime=None, image_path=None):
    self.datetime = datetime
    self.image_path = image_path
    print('(), ' + str(self.datetime))
    
  def __repr__(self):
    return '<Activity %s>' % (self.image_path)
  
  # http://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask
  @property 
  def serialize(self):
     # http://stackoverflow.com/questions/455580/json-datetime-between-python-and-javascript
     dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime) else None
     print('serialize, ' + str(self.datetime))
     return {
       'id'         : self.id,
       'datetime'   : self.datetime.isoformat(),
       'image_path' : self.image_path
     }
  
  @staticmethod
  def find(start, end):
    start_utc = start.astimezone(tz.tzutc())
    end_utc = end.astimezone(tz.tzutc())
    return Activity.query.filter(Activity.datetime >= start_utc, Activity.datetime <= end_utc).order_by(Activity.datetime.asc()).all()

class Weight(db.Model):
  __tablename__ = 'weight'
  
  id       = db.Column(db.Integer, primary_key=True)
  datetime = db.Column(db.DateTime(timezone=True))
  qty      = db.Column(db.Float)
  unit     = db.Column(db.String(20))
  
  def __init__(self, datetime, qty, unit='lb'):
    self.datetime = datetime
    self.qty = qty
    self.unit = unit
    
  def __repr__(self):
    return '<Weight %s %s>' % (self.qty, self.unit)
  
  @property 
  def serialize(self):
     dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime) else None
     return {
       'id'       : self.id,
       'datetime' : self.datetime.isoformat(),
       'qty'      : self.qty,
       'unit'     : self.unit
     }
     
  @staticmethod
  def find(start, end):
    start_utc = datetime.min if start is None else start.astimezone(tz.tzutc())
    end_utc = datetime.max if end is None else end.astimezone(tz.tzutc())
    return Weight.query.filter(Weight.datetime >= start_utc, Weight.datetime <= end_utc).order_by(Weight.datetime.asc()).all()
