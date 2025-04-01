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
from CustomModules import api_modules, db_modules

db_modules.create_database()

app = Flask(__name__)
app.secret_key = "secret hehe"
#app.secret_key = os.urandom(32)

#----------------------------------------------------------------------------------------------------------------

# Landing Page
@app.route('/', methods = ['GET', 'POST'])
def landing():
    return a;

#----------------------------------------------------------------------------------------------------------------

# Home Page
@app.route('/homepage', methods = ['GET', 'POST'])
def homepage():
    return a;

#----------------------------------------------------------------------------------------------------------------

# Login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    return a;

#----------------------------------------------------------------------------------------------------------------

# Logout
@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    return a;

#----------------------------------------------------------------------------------------------------------------

# Favorites
@app.route('/fav', methods = ['GET', 'POST'])
def fav():
    return a;

#----------------------------------------------------------------------------------------------------------------

# Search/Filter
@app.route('/search', methods = ['GET', 'POST'])
def search():
    return a;

#----------------------------------------------------------------------------------------------------------------

# Map
@app.route('/map', methods = ['GET', 'POST'])
def map():
    return a;

#----------------------------------------------------------------------------------------------------------------

# Infomation
@app.route('/info', methods = ['GET', 'POST'])
def info():
    return a;

#----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.debug = True
    app.run()
