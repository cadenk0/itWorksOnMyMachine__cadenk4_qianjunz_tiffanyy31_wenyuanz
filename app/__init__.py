#----------------------------------------------------------------------------------------------------------------

from flask import Flask, flash, render_template, request, redirect, url_for, session, flash, jsonify
import sqlite3, os, datetime, string, random, uuid, json, re, csv


import build_db
build_db.makeDb()


app = Flask(__name__)
app.secret_key = "secret hehe"
#app.secret_key = os.urandom(32)

def signed_in():
    return 'username' in session.keys() and session['username'] is not None

def check_user(username):
    user = build_db.get_user("username", username)
    print(user)
    if user is None:
        return False
    return user[0] == username

def check_password(username, password):
    user = build_db.get_user("username", username)
    if user is None:
        return False
    return user[1] == password


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
        username = request.form.get('username')
        password = request.form.get('password')
        if not check_user(username):
            flash("No such username exists")
            return render_template("login.html")
        if not check_password(username, password):
            flash("Incorrect password")
            return render_template("login.html")
        session['username'] = username
        return redirect(url_for('map'))
    return render_template("login.html")


# Sign Up
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if signed_in():
        return redirect(url_for('home'))
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = build_db.get_user("username", username)
        if user is None:
            build_db.add_account(username, password)
            return redirect('/login')
        else:
            flash("Username already exists")
            return render_template('register.html')
    return render_template("register.html")

#----------------------------------------------------------------------------------------------------------------

# Reading csv file
def listOfLocations():
    with open('whc-sites-2023.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        listOfData = {}
        first_row = next(reader)
        
        print(first_row[15])
            
            
        for row in reader:
            name = row[3]
            description = row[5]
            longitude = row[14]
            latitude = row[15]
            place = row[30].split(",")
            for state in place:
                build_db.add_landmark(name, state, description, latitude, longitude)
                listOfData[state] = listOfData.get(state, 0) + 1
        (k := next(iter(listOfData)), listOfData.pop(k))
        sorted_items = sorted(listOfData.items(), key=lambda item: item[1])
        remove_item = remove_irrelevant(sorted_items)
        #print(remove_item)
        returnable = "["
        for i in remove_item:
            returnable = returnable + '{ name: "' + i[0] + '", score: ' + str(i[1]) + " },"
        return returnable + "];"

## idk if we should be removing stuff

def remove_irrelevant(input_dict):
    while(len(input_dict) > 30):
        del input_dict[0]
    return input_dict

#----------------------------------------------------------------------------------------------------------------

# d4density
@app.route('/density', methods = ['GET', 'POST'])
def density():
    return render_template("d3density.html")

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

# Map
@app.route('/map', methods = ['GET', 'POST'])
def map():
    landmarks = build_db.get_landmark()
    countries = sorted(set(l['country'] for l in landmarks if l['country']))
    print(countries)
    return render_template("map.html", countries = countries, landmarks = landmarks)

#----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.debug = True
    app.run()
