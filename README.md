# Development

## Get Started
After git clone the project and cd the project directory, follow these one-time steps to setup the development environment.
```
brew install sqlite3
brew install db-browser-for-sqlite
brew install curl

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
