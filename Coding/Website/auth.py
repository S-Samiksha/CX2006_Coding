#do not delete 
from flask import Blueprint, render_template, request, url_for, flash
import mysql.connector
auth = Blueprint('auth', __name__) #much easier to call the same as the file

#replace each item with your own respective password, localhost etc. 
cur = mysql.connector.connect(user='root', password='password',
                    host='localhost',
                    database='cz2006')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")
#must use the POST method!
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        #still need to implement use case stuff, the one character, one number that thing
        if len(email) < 4:
            flash("Your Email is too short. Email must be greater than 4 characters", category='error')
        elif len(password)<5:
            flash("Your password is too short. Password must be greater than 8 characters", category='error')
        elif (password != password2):
            flash("Password and Confirm Password are not equal", category='error')
        else:
            #add user to database
            
            cursor = cur.cursor()
            statement = "INSERT INTO accounts (Email, Password) VALUES (%s, %s)"
            val = (email, password)
            cursor.execute(statement, val)
            cur.commit() 
            cursor.close()
            cur.close()
            flash("Account Created", category='success')


    
    return render_template("register.html")

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/profile')
def profile():
    #how to pass in variables from python into html
    #use {% %} to use if statement and for loops in python in html files
    #its called using jinja 
    return render_template("profile.html", user="Thomas")

@auth.route('/messages')
def messages():
    return render_template("messages.html")

@auth.route('/search_house')
def search_house():
    return render_template("search_house.html")

@auth.route('/update_roommate')
def update_roommate():
    return render_template("update_roommate.html")

@auth.route('/update_self')
def update_self():
    return render_template("update_self.html")

@auth.route('/view_houses')
def view_houses():
    return render_template("view_houses.html")