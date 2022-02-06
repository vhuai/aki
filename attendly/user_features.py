from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from attendly.db import get_db
from datetime import datetime
import json

bp = Blueprint('user_features', __name__, url_prefix='/user_features')

@bp.route('/view', methods=('GET', 'POST'))
def view():
  db = get_db()
  name = request.args.get("user_name")
  # GET one user features, return json
  if name is not None:
    results = db.execute(
      'SELECT features, time_stamp FROM user_features WHERE user_name = \'' + name + '\''
    ).fetchone()
    if results is None:
      return jsonify(success=False)
    return {"user_name": name, "features": results["features"], "time_stamp": results["time_stamp"]}

  # GET all user features. return html page
  results = db.execute(
    'SELECT user_name, features, time_stamp FROM user_features'
  ).fetchall()
  return render_template('view_features.html', userfeatures=results)

@bp.route('/record', methods=('PUT', 'POST'))
def record():
  db = get_db()
  # will later need conversion to true UTC with pytz
  time = datetime.utcnow().strftime("%Y-%M-%d %H:%m:%S")
  print(time)
  data = json.loads(request.data)
  # optional: ensure data has "name" and "features" (float array)
  db.execute(
    'INSERT OR REPLACE INTO user_features VALUES (?, ?, ?)',
    (data["user_name"], str(data['features']), time))
  db.commit()
  return jsonify(success=True)
