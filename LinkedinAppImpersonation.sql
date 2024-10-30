/*Using LinkedIn Posts data
to create SQL Statements*/

/*Creating a Linkedin database*/
CREATE DATABASE LinkedIn_Post_Groupfour;

/*Creating a table to store Linkedin posts data*/
CREATE TABLE Posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username TEXT,
    content TEXT,
    post_date DATE,
    likes INT,
    comments INT
);

/*Insert values into the table*/ 
INSERT INTO Posts (username, content, post_date, likes, comments) VALUES ("Joyce Yayra Osafo", "Just completed the Associate Data Analyst certification on Data Camp","24-10-24", 200, 150);
INSERT INTO Posts (username, content, post_date, likes, comments) VALUES ("Joyce Yayra Osafo", "Stay motivated, the best is yet to come","24-09-24", 350, 250);
INSERT INTO Posts (username, content, post_date, likes, comments) VALUES ("Joyce Yayra Osafo", "Meet my mentors, they are the best","24-08-24", 400, 150);
INSERT INTO Posts (username, content, post_date, likes, comments) VALUES ("Joyce Yayra Osafo", "Excited to join the Big data US Team","24-07-24", 250, 90);
INSERT INTO Posts (username, content, post_date, likes, comments) VALUES ("Joyce Yayra Osafo", "Had an amazing time volunteering at the GDIW Event","24-06-24", 120, 100);
INSERT INTO Posts (username, content, post_date, likes, comments) VALUES ("Joyce Yayra Osafo", "Change and Innovation:My GDIW'24 Experience","24-05-24", 980, 300);
INSERT INTO Posts (username, content, post_date, likes, comments) VALUES ("Joyce Yayra Osafo", "I am now equipped to tackle complex challenges in Python","24-04-24", 500, 120);
INSERT INTO Posts (username, content, post_date, likes, comments) VALUES ("Joyce Yayra Osafo", "Just levelled up my data skills with 9 certifications from DataCamp","24-03-24", 700, 480);
INSERT INTO Posts (username, content, post_date, likes, comments) VALUES ("Joyce Yayra Osafo", "Just completed the Intermediate SQL certification on Data Camp","24-02-24", 190, 50);
INSERT INTO Posts (username, content, post_date, likes, comments) VALUES ("Joyce Yayra Osafo", "Just completed the Intermediate Power BI on Data Camp","24-01-24", 3900, 2000);

/*Viewing the LinkedIn_Post_Groupfour table*/ 
SELECT 
    *
FROM
    Posts;

/*Updating two posts from the table*/ 
UPDATE Posts 
SET 
    content = 'Just completed the AWS Cloud Certification on DataCamp'
WHERE
    id = 10;

/*Update two*/
UPDATE Posts 
SET 
    content = 'How i bought my new Tesla Model Y 2024'
WHERE
    id = 9;

/*Deleting two posts from table*/
DELETE FROM Posts 
WHERE
    id = 5;

/*Second deletion*/
DELETE FROM Posts 
WHERE
    id = 4;
    
/*Viewing the final content of the LinkedIn_Post_Groupfourtable*/ 
SELECT 
    *
FROM
    Posts;