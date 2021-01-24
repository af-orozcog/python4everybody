import json
import sqlite3

connection = sqlite3.connect("rosterDB.sqlite")
cur = connection.cursor()

scripToRun = """ 
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;

    CREATE TABLE User(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Course(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );
    CREATE TABLE Member(
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id, course_id)
    );
"""
cur.executescript(scripToRun)

filename = input("Please enter the file name:")

wholeFile = open(filename).read()
json_data = json.loads(wholeFile)

for value in json_data:

    personName = value[0]
    courseName = value[1]
    role = value[2]

    print("Name:",personName,"course Name:",courseName,"the role:",role)

    cur.execute("""
    INSERT OR IGNORE INTO User (name) VALUES
    (?)
    """, (personName,))

    cur.execute("""
    INSERT OR IGNORE INTO Course (title) VALUES
    (?)
    """, (courseName,))
    cur.execute("""
    SELECT id FROM Course WHERE title = ?
    """, (courseName,))
    idCourse = cur.fetchone()[0]
    cur.execute("""
    SELECT id FROM User WHERE name = ?
    """,(personName,))
    idPerson = cur.fetchone()[0]

    cur.execute("""
    INSERT OR REPLACE INTO Member 
    (user_id,course_id,role) VALUES (?, ? , ?)
    """,(idPerson,idCourse,role))

    connection.commit()