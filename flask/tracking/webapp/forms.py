from flask.ext.wtf import Form
from wtforms import DecimalField, SubmitField
from wtforms.validators import Required

class EntryForm(Form):
  qty = DecimalField('Qty', places=1, rounding=None, validators=[Required()])
  submit = SubmitField('Submit')