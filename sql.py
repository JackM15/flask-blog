#---- SQL.py : Create a SQLite3 table and populate it with data ----#

import sqlite3

#create a new DB if it doesn't exist
with sqlite3.connect("blog.db") as db:
    #get a curssor used to execute SQL
    cursor = db.cursor()

    #create the table
    cursor.execute("""
        CREATE TABLE posts
        (title TEXT, post TEXT)
        """)
    
    #insert dummy data into table
    cursor.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    cursor.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    cursor.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    cursor.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
    