# AKi is a web application connected to a camera system that uses Face Recognition to take attendance of classrooms when students are entering the door. It saves time and is highly accurate.
![image](https://user-images.githubusercontent.com/83354426/152682836-4ce4ed8f-33a8-4fed-a279-3af200531ebe.png)
[![AKi Video]({https://www.youtube.com/watch?v=uB52tE804CY})]({https://www.youtube.com/watch?v=uB52tE804CY} "AKi First Web Application with Face Recognition for Taking Attendance in Schools | GunnHacks 8.0")


Every day, hours are wasted taking attendance of students when they enter the class. We identified this problem and decide to find a solution. Aki is a system that leverages the power of Artificial Intelligence and Face Recognition to take attendance of students when they are entering the classroom. We created a web application that receives immediate input from the small cameras in every classroom door, it crosses the information with students' schedules and profiles and creates an accurate report of attendance every single day.

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
