# Aki is a web application that uses Facial Recognition to make attendance of class with the most accuracy.
![image](https://user-images.githubusercontent.com/83354426/152682836-4ce4ed8f-33a8-4fed-a279-3af200531ebe.png)


Taking attendance in our regular class takes a long time. Even with newer technologies like RFID, we need to take attendance individually from every student. In this age of Artificial Intelligence, we can make the attendance system much easier where we don't need to spend a single moment to take attendance.
All details of the students are stored in the cloud. With the Machine learning algorithm, the app detects the faces matches with the data stored in the cloud and then authenticates it.
Once it authenticates the face it stores the student name with the exact time of attendance. It keeps the record in an excel sheet which will then be converted into a detailed report.

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
