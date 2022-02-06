import os

from flask import Flask
from flask import render_template, redirect

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)

  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'attendly.sqlite'),
  )

  # use test config is set
  if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_mapping(test_config)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    # TODO: log error
    pass

  from . import db
  db.init_app(app)

  from . import attendence
  app.register_blueprint(attendence.bp)

  from . import user
  app.register_blueprint(user.bp)

  # a quick test to see if the server is alive
  @app.route('/ping')
  def ping():
    from datetime import datetime
    return 'pong at ' + datetime.now().isoformat()

  @app.route('/')
  def index():
    return render_template('index.html')

  return app
