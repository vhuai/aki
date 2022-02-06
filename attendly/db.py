from fileinput import filename
import sqlite3
import xxlimited
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
  if 'db' not in g:
    g.db = sqlite3.connect(
      current_app.config['DATABASE'],
      detect_types=sqlite3.PARSE_DECLTYPES
    )
    g.db.row_factory = sqlite3.Row

  return g.db

def close_db(e=None):
  db = g.pop('db', None)
  if db is not None:
    db.close()

def init_db():
  db = get_db()
  with current_app.open_resource('schema.sql') as f:
    db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
  """Create the new database for attendly"""
  init_db()
  click.echo('Created the new database.')

@click.command('import-user-features')
@click.argument('filename')
@with_appcontext
def import_user_features_command(filename):
  """Import user,timestamp from a csv file"""
  with open(filename, 'r') as f:
    db = get_db()
    count = 0
    for line in f.readlines():
      x = line.split(',')
      if len(x) != 2:
        continue
      db.execute(
        'INSERT OR REPLACE INTO user_features VALUES (?, ?, ?)',
        (x[0].strip(), '[]', x[1].strip()))
      count += 1
    if count > 0:
      db.commit()
    click.echo("imported %d records" % count)

def init_app(app):
  app.teardown_appcontext(close_db)
  app.cli.add_command(init_db_command)
  app.cli.add_command(import_user_features_command)
