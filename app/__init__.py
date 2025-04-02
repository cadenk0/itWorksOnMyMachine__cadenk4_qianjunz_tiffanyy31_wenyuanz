#----------------------------------------------------------------------------------------------------------------

from flask import Flask, flash, render_template, request, redirect, url_for, session, flash, jsonify
import sqlite3
import os
import datetime
import string
import random
import uuid
import json
import re


app = Flask(__name__)
app.secret_key = "secret hehe"
#app.secret_key = os.urandom(32)

#----------------------------------------------------------------------------------------------------------------

# Landing Page
@app.route('/', methods = ['GET', 'POST'])
def landing():
    return redirect(url_for('homepage'))

#----------------------------------------------------------------------------------------------------------------

# Home Page
@app.route('/homepage', methods = ['GET', 'POST'])
def homepage():
    if 'username' in session:
        return render_template("homepage.html", logged_in = True, username = session['username'])
    return render_template("homepage.html")

#----------------------------------------------------------------------------------------------------------------

# Login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('homepage'))
    if request.method == 'POST':
        #input checking for username
        return redirect(url_for('homepage'))
    return render_template("login.html")

#----------------------------------------------------------------------------------------------------------------

# Sign Up
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template("signup.html")

#----------------------------------------------------------------------------------------------------------------

# Logout
@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('homepage'))

#----------------------------------------------------------------------------------------------------------------

# Favorites
@app.route('/fav', methods = ['GET', 'POST'])
def fav():
    return render_template("favorites.html")

#----------------------------------------------------------------------------------------------------------------

# Search/Filter
@app.route('/search', methods = ['GET', 'POST'])
def search():
    return render_template("search.html")

#----------------------------------------------------------------------------------------------------------------

# Map
@app.route('/map', methods = ['GET', 'POST'])
def map():
    return render_template("map.html")

#----------------------------------------------------------------------------------------------------------------

# Infomation
@app.route('/info', methods = ['GET', 'POST'])
def info():
    return render_template("info.html")

#----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.debug = True
    app.run()
