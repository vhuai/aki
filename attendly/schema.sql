DROP TABLE IF EXISTS attendence_record;
DROP TABLE IF EXISTS user_features;

CREATE TABLE attendence_record (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_name TEXT NOT NULL,
  event_loc TEXT NOT NULL,
  event_time TEXT NOT NULL
);

CREATE TABLE user_features (
  user_name TEXT NOT NULL UNIQUE,
  features TEXT NOT NULL,  -- sample: [12.3, 23.4, 34.5]
  time_stamp TEXT
);
