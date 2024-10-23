
CREATE TABLE aircraft (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    registration TEXT NOT NULL UNIQUE,
    flight_hours REAL DEFAULT 0,
    last_maintenance_date TEXT,
    next_maintenance_date TEXT
);

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
