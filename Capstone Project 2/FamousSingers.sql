-- creating a table for movie stars
CREATE TABLE famous_singers(id INTEGER PRIMARY KEY AUTO_INCREMENT, first_name TEXT, last_name TEXT, gender TEXT);


-- inserting records into movie star table
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Bruno", "Mars", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Rihanna", "Fenty", "Female");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Lady", "Gaga", "Female");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Justin", "Bieber", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("The", "Weeknd", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Billie", "Eilish", "Female");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Drake", "Graham", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Kirk", "Franklin", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Tasha", "Cobbs Leonard", "Female");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Ariana", "Grande", "Female");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Dua", "Lipa", "Female");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Donnie", "McClurkin", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Fred", "Hammond Jr.", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Israel", "Houghton", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("CeCe", "Winans", "Female");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("BeBe", "Winans", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Byron", "Cage", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Mary", "Mary", "Female");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Jonathan", "McReynolds", "Male");
INSERT INTO famous_singers (first_name, last_name, gender) VALUES
("Tye", "Tribbett", "Male");

-- querying singers table
SELECT *
FROM famous_singers;


-- creating a new table called songs
CREATE TABLE songs(id INTEGER PRIMARY KEY AUTO_INCREMENT, title TEXT, Genre TEXT);

-- adding records to the songs table
INSERT INTO songs (Title, Genre) VALUES
  ("Just the Way You Are", "Pop"),
  ("Umbrella", "Pop"),
  ("Poker Face", "Pop"),
  ("Baby", "Pop"),
  ("Blinding Lights", "Pop"),
  ("Bad Guy", "Pop"),
  ("God's Plan", "Hip hop"),
  ("Stomp", "Gospel"),
  ("You Did It Again", "Gospel"),
  ("Thank U, Next", "Pop"),
  ("New Rules", "Pop"),
  ("The Prayer", "Gospel"),
  ("I Can Only Imagine", "Contemporary Christian"),
  ("Amazing Grace", "Hymn"),
  ("Always Be My Baby", "Gospel"),
  ("Total Praise", "Gospel"),
  ("I'll Be Alright", "Gospel"),
  ("Shackles (Praise Break)", "Gospel"),
  ("Favor", "Gospel"),
  ("Victory", "Gospel");
  
  -- querying songs table
  SELECT *
  FROM songs;
  

-- creating a last table called location
CREATE TABLE location(id INTEGER PRIMARY KEY AUTO_INCREMENT,city TEXT,country TEXT);

-- add records to the location table
INSERT INTO location(city,country) VALUES
("Honolulu", "USA"),
("Bridgetown", "Barbados"),
("Manhattan", "USA"),
("London", "Canada"),
("Scarborough", "Canada"),
("Los Angeles", "USA"),
("Toronto", "Canada"),
("Fort Worth", "USA"),
("Atlanta", "USA"),
("Boca Raton", "USA"),
("London", "UK"),
("New York", "USA"),
("Detroit", "USA"),
("Chicago", "USA"),
("Detroit", "USA"),
("Detroit", "USA"),
("New Orleans", "USA"),
("Chicago", "USA"),
("Chicago", "USA"),
("Philadelphia", "USA");

-- querying the location table
SELECT *
FROM location;


-- join the singers, songs, and location table
SELECT fs.id, fs.first_name,fs.last_name, fs.gender,l.city, l.country, so.title, so.genre
FROM famous_singers AS fs
JOIN songs AS so
ON fs.id = so.id
JOIN location AS l
ON fs.id = l.id; 
