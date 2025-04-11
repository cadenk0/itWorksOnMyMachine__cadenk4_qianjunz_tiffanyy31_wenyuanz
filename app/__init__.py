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
        listOfData = {}
        for row in reader:
            place = row[30].split(",")
            #print(place)
            for state in place:
                aqui = False
                for takenState in listOfData:
                    if state == takenState:
                        listOfData[state] = listOfData[state] + 1
                        aqui = True
                if not aqui:
                    listOfData[state] = 1
                    aqui = False
        (k := next(iter(listOfData)), listOfData.pop(k))
        returnable = "["
        for i in listOfData:
            returnable = returnable + '{ name: "' + i + '", score: ' + str(listOfData[i]) + " },"
        return returnable + "];"

#print(listOfLocations())
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

def get_sites():
    with open('whc-sites-2023.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader) 
        sites = []
        for row in reader:
            site = {
                'name': row[1],    
                'country': row[2],  
                'latitude': row[14],
                'longitude': row[15],
            }
            sites.append(site)
        return sites

# Search/Filter
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()
    sites = get_sites()
    results = []
    if query:
        for site in sites:
            if (query in site['name'].lower()) or (query in site['country'].lower()):
                results.append(site)
    return render_template("search.html", results=results, query=query)

#----------------------------------------------------------------------------------------------------------------

# Map
@app.route('/map', methods = ['GET', 'POST'])
def map():
    data = listOfLocations()[1:]
    return render_template("map.html", map = data)

#----------------------------------------------------------------------------------------------------------------

# Infomation
@app.route('/info', methods = ['GET', 'POST'])
def info():
    return render_template("info.html")

#----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.debug = True
    app.run()
