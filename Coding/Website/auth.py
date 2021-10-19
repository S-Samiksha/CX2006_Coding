#do not delete 
from flask import Blueprint, render_template, request, url_for, flash
import mysql.connector
auth = Blueprint('auth', __name__)
current_account_id = 0

"""
PLEASE READ!!
Instructions:
Here are all the variables we can use to pass into each html file. 
From the logout page, we get a current_account_id which is the PK for the sql then everyone can use from there!
current_user will be the NAME of the user this is to be standardized by everyone using this file 

email, password, password2, current_user, age, gender, occupation, ethnicity, imgpath, r_gender, r_age, r_occupation, r_ethnicity 
will be used as variables names. KEEP TO THESE VARIABLE NAMES FOR EASE OF USE
"""


#------------------------------------------------------------MySql Connector-----------------------------------------------------------------------
#replace each item with your own respective password, localhost etc. 
cur = mysql.connector.connect(user='root', password='password',
                    host='127.0.0.1',
                    database='cz2006')



# ----------------------------------------------------Start Login--------------------------------------------------------------------------------
#still need to implement
#this was partially done to do the other html pages
#needs to be implemented as per use case
#changed the id to email and password in login and register 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    global current_account_id
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        cursor = cur.cursor()
        statement = "SELECT AccountID from accounts where Email = %s"
        val = (email, )
        cursor.execute(statement, val)
        current_account_id = cursor.fetchone()
        print(current_account_id)
        home()
    return render_template("login.html")
#must use the POST method!

#-----------------------------------------------------End Login---------------------------------------------------------------------------------


#----------------------------------------------------Start Register------------------------------------------------------------------------------
#still need to be implemented based on use case 
#the button also does not close when clicking the cross button --> can just remove it was just to test the sql and the python statements
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
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
#---------------------------------------------------End Register----------------------------------------------------------------------------------


#---------------------------------------------------Start Home and Roommate Reccommendation------------------------------------------------------
@auth.route('/home')
def home():
    cursor = cur.cursor()
    statement = "SELECT * from profile where accounts_AccountID = %s"
    val = current_account_id
    cursor.execute(statement, val)
    profiletuple = cursor.fetchall()
    print(profiletuple)
    #cur.close()

    return render_template("home.html")

#-------------------------------------------------End Home----------------------------------------------------------------------------------------


#------------------------------------------------Start profile------------------------------------------------------------------------------------
@auth.route('/profile')
def profile():
    #how to pass in variables from python into html
    #use {% %} to use if statement and for loops in python in html files
    #its called using jinja 
    #pass in variable called current_user into the profile.html page
    return render_template("profile.html", current_user)
#-----------------------------------------------End Profile---------------------------------------------------------------------------------------



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