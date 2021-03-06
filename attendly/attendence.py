from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from attendly.db import get_db

bp = Blueprint('attendence', __name__, url_prefix='/attendence')

@bp.route('/view', methods=('GET', 'POST'))
def view():
  db = get_db()
  results = db.execute(
    'SELECT user_name, event_loc, event_time FROM attendence_record ORDER BY id ASC'
  ).fetchall()
  return render_template('view_attendence.html', attendence=results)

@bp.route('/record', methods=('GET', 'POST'))
def record():
  if request.method == 'POST':
    db = get_db()
    db.execute(
      'INSERT INTO attendence_record (user_name, event_loc, event_time) VALUES (?, ?, ?)',
      (request.form['user_name'], request.form['event_loc'], request.form['event_time']))
    db.commit()
    return redirect(url_for('attendence.view'))
  else:
    return render_template('record_attendence.html')