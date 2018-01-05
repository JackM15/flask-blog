#---- blog.py - The controller ----

# imports
from flask import Flask, render_template, request, session, \
    flask, redirect, url_for, g
import sqlite3

# configuration
DATABASE = 'blog.db'

app = Flask(__name__)

# pulls in cap configuration by looking for uppercase variables
app.config.from_object(__name__)

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run(debug=True)