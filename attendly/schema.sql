DROP TABLE IF EXISTS attendence_record;

CREATE TABLE attendence_record (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_name TEXT NOT NULL,
  event_loc TEXT NOT NULL,
  event_time TEXT NOT NULL
);
