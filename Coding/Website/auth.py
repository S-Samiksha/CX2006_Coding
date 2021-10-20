#do not delete 

from flask import Blueprint, render_template, request, url_for, flash, redirect, jsonify
import pandas as pd
import json

import mysql.connector
auth = Blueprint('auth', __name__)
current_account_id = 0

"""
PLEASE READ!!
From the login page, we get a current_account_id then everyone can use from there!
to use, global current_account_id is called in the login page --> do not remove 
Each page is separated with the line #------ like that

connect with sql, localhost and your own password

Below for code reference:
"""

"""
import request done at the top, import API as pandas DF
r = requests.get('url') #paste url here
j = r.json()
table = pd.DataFrame.from_dict(j)
"""
"""
pandas code format for filtering:
table = table[table.<variable_name> != <value>]
table = table[table.<variable_name> == <value>]
table = table[table.<variable_name> > <value>]
table = table[table.<variable_name> < <value>]

size = table.size / (no. of columns in table) = no. of rows in table

table = table.values.tolist() #convert to list before 
pass in table into render_template as table=table 
then in html file {{table[x][y]}} to call the values 

"""

"""
My SQl -- python reference 
cursor = cur.cursor()
#separate the statment and the values 
statement = "SELECT AccountID from accounts where Email = %s" #place SQL query here 
val = (email, )
cursor.execute(statement, val)
current_account_id = cursor.fetchone() #fetch one means fetch only one column 
#fetchall means fetch all columns 

#insert data into sql database
cursor = cur.cursor()
statement = "INSERT INTO accounts (Email, Password) VALUES (%s, %s)" # we can do it this way too?
val = (email, password)
cursor.execute(statement, val)
cur.commit() #commit to sql

#update for one account at a particular place must concatenate string if separated and cannot use VALUES (%s, %s) 
#why is this so?
statement = 'UPDATE profile SET r_Skip = '+str(AiD)+' WHERE accounts_AccountID = %s'

"""

"""
references:
https://www.youtube.com/watch?v=dam0GPOAvVI
https://www.w3schools.com/python/python_mysql_getstarted.asp 

"""


#------------------------------------------------------------MySql Connector-----------------------------------------------------------------------
#replace each item with your own respective password, localhost etc. 
cur = mysql.connector.connect(user='root', password='password',
                    host='localhost',
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
        #print(current_account_id)
        return redirect(url_for('auth.home'))
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
@auth.route('/home', methods=['GET', 'POST'])
def home():
    #how to get from SQL
    cursor = cur.cursor()
    statement = "SELECT * from profile where accounts_AccountID = %s"
    val = current_account_id
    cursor.execute(statement, val)
    profilelist = cursor.fetchall()
    Name = [item[5] for item in profilelist]
    Name = Name[0]
    #cur.close()
    r_gender = [item[6] for item in profilelist]
    r_gender = r_gender[0]
    r_age = [item[7] for item in profilelist]
    r_age = r_age[0]
    skip = [item[8] for item in profilelist]
    skip = skip[0]
    r_occupation = [item[9] for item in profilelist]
    r_occupation = r_occupation[0]
    r_ethnicity = [item[10] for item in profilelist]
    r_ethnicity = r_ethnicity[0]
    statement = 'SELECT * from profile'
    #need to account for language 
    cursor.execute(statement)
    table = cursor.fetchall()
    statement = 'SELECT * from user_language where accounts_AccountID = %s'
    val = current_account_id
    #need to account for language 
    cursor.execute(statement, val)
    u_lan = cursor.fetchall()
    u_lan = [item[0] for item in u_lan]
    u_lan = u_lan[0]
    #print(u_lan)
    statement = 'SELECT * from roommate_language'
    #need to account for language 
    cursor.execute(statement)
    r_lan = cursor.fetchall()
    #converting to pandas dataframe
    table = pd.DataFrame(table, columns = ['Age', 'Gender', 'Occupation', 'Ethnicity', 'ImgPathFile', 'Name', 'R_Gender', 'R_Age', 'R_Skip', 'R_Occupation', 'R_Ethnicity', 'accountsID'])
    r_lan = pd.DataFrame(r_lan, columns = ['r_lang', 'accountsID'])
    table = pd.merge(table, r_lan, left_on='accountsID', right_on='accountsID', how='left')
    table = table[table.accountsID != current_account_id] #remove the current person 
    table = table[table.accountsID != skip]
    table = table[table.R_Age > (r_age-2)]
    table = table[table.R_Age < (r_age+2)]
    #print(table.size)
    if (r_gender != 'Any' and table.size>5):
        table = table[table.R_Gender == r_gender]
    elif (r_occupation != 'Any' and table.size>5):
        table = table[table.R_Occupation == r_occupation]
    elif (r_ethnicity != 'Any' and table.size>5):
        table = table[table.R_Ethnicity == r_ethnicity]
    elif (u_lan != 'Any' and table.size>5):
        table = table[table.r_lang == u_lan]

    size = int(table.size)
    size = int(size/12)
    i=0
    table = table.values.tolist()
    return render_template("home.html", Name = Name, table=table, size = size, i=i)


#for button manipulation from js, link in home.js and home.html commented as 'button-sql-js-flask-connection'
@auth.route('/delete-rec', methods=['POST'])
def delete_rec():
    AiD = json.loads(request.data)
    AiD = AiD['AiD']
    #print(AiD)
    cursor = cur.cursor()
    #to pass in update to sql
    #concatenate
    statement = 'UPDATE profile SET r_Skip = '+str(AiD)+' WHERE accounts_AccountID = %s'
    val = (current_account_id)
    cursor.execute(statement, val)
    #cursor.execute(statement, val)

    cur.commit()


    return jsonify({})
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


#-----------------------------------------------Start Messages------------------------------------------------------------------------------------
@auth.route('/messages')
def messages():
    return render_template("messages.html")


#----------------------------------------------End Messages---------------------------------------------------------------------------------------

#---------------------------------------------Start Search/view Houses---------------------------------------------------------------------------------


@auth.route('/search_house')
def search_house():
    return render_template("search_house.html")


@auth.route('/view_houses')
def view_houses():
    return render_template("view_houses.html")

#--------------------------------------------End Search/view Houses------------------------------------------------------------------------------------

#-------------------------------------------Start Update Roommate---------------------------------------------------------------------------------
@auth.route('/update_roommate')
def update_roommate():
    return render_template("update_roommate.html")

#--------------------------------------------End Update Roommate-----------------------------------------------------------------------------------

#-------------------------------------------Start Update Self--------------------------------------------------------------------------------------
@auth.route('/update_self')
def update_self():
    return render_template("update_self.html")

#--------------------------------------------End Update Self---------------------------------------------------------------------------------------

