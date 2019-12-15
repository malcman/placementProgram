CREATE TABLE users (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  fullname VARCHAR(100) NOT NULL,
  email VARCHAR(40) NOT NULL UNIQUE,
  avatar VARCHAR(256) NOT NULL,
  tokens TEXT,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);