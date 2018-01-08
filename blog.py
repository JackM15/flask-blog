#---- blog.py - The controller ----

# imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3
from functools import wraps

# configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'thisisonlyfortestingsoisuselessandnotsecure'

app = Flask(__name__)

# pulls in cap configuration by looking for uppercase variables
app.config.from_object(__name__)

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('login'))
    return wrap

# routes
@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    status_code = 200
    #if its a post request do the following
    if request.method == 'POST':
        #if the entered info doesnt match the username/pass in the config, give an error
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
                error = 'Invalid Credentials. Plesae try again.'
                status_code = 401
        else:
            #set session to logged in and redirect to the main page
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template("login.html", error=error), status_code

@app.route("/logout")
def logout():
    session.pop('logged_in', None) #reset session key back to default value
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route("/main")
@login_required
def main():
    return render_template("main.html")

#run the app if launched from this file
if __name__ == '__main__':
    app.run(debug=True)