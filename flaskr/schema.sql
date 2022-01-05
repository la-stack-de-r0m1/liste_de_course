DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS shopping_list;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE stock (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  owner_id INTEGER NOT NULL,
  content TEXT NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES user (id)
);

CREATE TABLE shopping_list (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  owner_id INTEGER NOT NULL,
  content TEXT NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES user (id)
);

