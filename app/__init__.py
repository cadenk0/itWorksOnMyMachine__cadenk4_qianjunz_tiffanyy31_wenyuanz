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
    return render_template("homepage.html")

#----------------------------------------------------------------------------------------------------------------

# Login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html")

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
    return render_template("homepage.html")

#----------------------------------------------------------------------------------------------------------------

# Search/Filter
@app.route('/search', methods = ['GET', 'POST'])
def search():
    return render_template("homepage.html")

#----------------------------------------------------------------------------------------------------------------

# Map
@app.route('/map', methods = ['GET', 'POST'])
def map():
    return render_template("homepage.html")

#----------------------------------------------------------------------------------------------------------------

# Infomation
@app.route('/info', methods = ['GET', 'POST'])
def info():
    return render_template("homepage.html")

#----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.debug = True
    app.run()
