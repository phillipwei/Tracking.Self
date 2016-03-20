from flask import Blueprint, render_template, request
from flask.ext.login import current_user, login_required

from .forms import EntryForm
from ..api import api

webapp = Blueprint('webapp', __name__, url_prefix='/app')

@webapp.route('/timeline', methods = ['GET', 'POST'])
@login_required
def timeline():
  return render_template('webapp/timeline.html')
  
@webapp.route('/entry')
@login_required
def entry():
  entry_form  = EntryForm()
  return render_template('webapp/entry.html', page_title='Entry', entry=entry_form)

# exploration -- weight
@webapp.route('/weight')
@login_required
def weight():
  return render_template('webapp/weight.html')
