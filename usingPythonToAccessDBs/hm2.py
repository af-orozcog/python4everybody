import xml.etree.ElementTree as ET
import sqlite3

#Method to look up for a key given the special xml format
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


connection = sqlite3.connect("itunes.sqlite")
cur = connection.cursor()

#make the new tables
creatingTables = """ 
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
"""
cur.executescript(creatingTables)

fileName = input("Please type the name of the file: ")

reader = ET.parse(fileName)
needed = reader.findall("dict/dict/dict")
print("valid entries:",len(needed))
for value in needed:
    if  lookup(value, 'Track ID') is None  : continue

    name = lookup(value, 'Name')
    artist = lookup(value, 'Artist')
    album = lookup(value, 'Album')
    count = lookup(value, 'Play Count')
    rating = lookup(value, 'Rating')
    genre = lookup(value,"Genre")
    length = lookup(value, 'Total Time')

    if name is None or artist is None or album is None or genre is None: 
        continue

    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute(""" INSERT OR IGNORE INTO Genre (name) VALUES ( ?)""" , (genre,))
    
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    
    artist_id = cur.fetchone()[0]
    cur.execute("SELECT id FROM Genre WHERE name = ? ", (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id,genre_id ,len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id,genre_id,length, rating, count,) )

    connection.commit()