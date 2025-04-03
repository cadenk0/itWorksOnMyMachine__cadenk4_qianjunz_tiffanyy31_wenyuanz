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
import csv


app = Flask(__name__)
app.secret_key = "secret hehe"
#app.secret_key = os.urandom(32)

#----------------------------------------------------------------------------------------------------------------

# Landing Page
@app.route('/', methods = ['GET', 'POST'])
def landing():
    return redirect(url_for('home'))

#----------------------------------------------------------------------------------------------------------------

# Home Page
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template("home.html", logged_in = True, username = session['username'])
    return render_template("home.html")

#----------------------------------------------------------------------------------------------------------------

# Login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        #input checking for username
        return redirect(url_for('home'))
    return render_template("login.html")

#----------------------------------------------------------------------------------------------------------------

# Reading csv file
def listOfLocations():
    with open('whc-sites-2023.csv') as file:
        reader = csv.reader(file)
        listOfData = []
        for row in reader:
            listOfData.append(row[14] + "," + row[15])
    return listOfData

print(listOfLocations())

#----------------------------------------------------------------------------------------------------------------

# Sign Up
@app.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template("register.html")

#----------------------------------------------------------------------------------------------------------------

# Logout
@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

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
