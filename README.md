# Development

## Get Started
After git clone the project and cd the project directory, follow these are one-time steps to setup the development environment.
```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

Create the attendly database to store user data
```
$ export FLASK_APP=attendly
$ export FLASK_ENV=development
$ flask init-db
```

**Optional Tools**

Use DB Browser for SQLite to browse user database
```
brew cask install db-browser-for-sqlite
```

## Run on Command Line
```
$ . venv/bin/activate
$ export FLASK_APP=attendly
$ export FLASK_ENV=development
$ flask run
```

## Highlights

Currently supported use cases
* Create an attendence record
* Show a list of all attendence records

Selected engineering notes
* Attendence records are stored in a local sqlite3 database
