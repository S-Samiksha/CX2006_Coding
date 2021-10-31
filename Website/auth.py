#do not delete 

from flask import Blueprint, render_template, request, url_for, flash, redirect, jsonify, session
import pandas as pd
import json
import requests
import mysql.connector
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)
current_account_id = 0
user_name = ""
user_age = ""
user_gender = ""
user_occupation  = ""
user_ethnicity  = ""
user_language = ""
user_profile_pic = ""


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
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'pwd' in request.form:
        details = request.form
        username = details['username']
        password = details['pwd']
        cursor = cur.cursor()
        cursor.execute('SELECT * FROM accounts WHERE Email = %s AND Password = %s', (username, password, ))
        account = cursor.fetchone()
        #query1 = ("SELECT * FROM accounts WHERE Email = username")
        #cursor.execute(query1)
        #frame = pd.DataFrame(cursor.fetchall())
        #print(frame)
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            current_account_id = session['id'] 
            session['username'] = account[1]
            msg = 'Logged in successfully!'
            return redirect(url_for('auth.home'))
        else:
            msg = 'Incorrect username/password'
    
    #return render_template('login.html')
    return render_template('login.html', msg = msg)
#must use the POST method!

#-----------------------------------------------------End Login---------------------------------------------------------------------------------


#----------------------------------------------------Start Register------------------------------------------------------------------------------
#still need to be implemented based on use case 
#the button also does not close when clicking the cross button --> can just remove it was just to test the sql and the python statements
@auth.route('/register', methods=['GET', 'POST'])
def register():
    
    msg = ''
    if request.method=='POST'  and 'username' in request.form and 'pwd' in request.form and 'confirmpwd' in request.form :
        details = request.form
        username = details['username']
        password = details['pwd']
        confirmpassword = details['confirmpwd']

        if password != confirmpassword:
            msg = "The passwords don't match!"
        if len(username) < 4:
            flash("Your Email is too short. Email must be greater than 4 characters", category='error')
        elif len(password)<8:
            flash("Password and Confirm Password are not equal", category='error')
        else:
            cursor = cur.cursor(buffered = True)
            
            query4 = ("SELECT MAX(AccountID) FROM accounts")
            cursor.execute(query4)
            newid = cursor.fetchone()[0]
            newid+=1
            
            #query1 = ("INSERT INTO accounts VALUES (%d, %s, %s)", (newid, username, password, ))
            cursor.execute("INSERT INTO accounts VALUES (%s, %s, %s)", (newid, username, password, ))
            cur.commit()
            msg = 'You have successfully registered!'
            #frame = pd.DataFrame(cursor.fetchall())
            #print(frame)
            session['loggedin'] = True
            session['id'] = newid
            current_account_id = session['id'] 
            session['username'] = username
            return redirect(url_for('auth.update_self'))
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    
    return render_template('register.html', msg = msg)
#---------------------------------------------------End Register----------------------------------------------------------------------------------


#---------------------------------------------------Start Home and Roommate Reccommendation------------------------------------------------------
@auth.route('/home', methods=['GET', 'POST'])
def home():
    #how to get from SQL
    global user_age 
    global user_gender
    global user_occupation 
    global user_ethnicity 
    global user_language
    global user_name
    global user_profile_pic
    cursor = cur.cursor()   
    #val = session['id'] 
    statement = ("SELECT * FROM profile WHERE accounts_AccountID = %s")
    cursor.execute(statement, (current_account_id, ))
    profilelist = cursor.fetchall()
    Name = [item[5] for item in profilelist]
    user_name = Name[0]
    Gender = [item[1] for item in profilelist]
    user_gender = Gender[0]
    Age = [item[0] for item in profilelist]
    user_age = Age[0]
    Occupation = [item[2] for item in profilelist]
    user_occupation = Occupation[0]
    Ethnicity = [item[3] for item in profilelist]
    user_ethnicity = Ethnicity[0]
    profile_pic = [item[4] for item in profilelist]
    user_profile_pic = profile_pic[0]
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
    cursor.execute(statement, (val,))
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
    
    return render_template("home.html", Name = user_name, table=table, size = size, i=i)




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
    val = (current_account_id, )
    cursor.execute(statement, val)
    #cursor.execute(statement, val)

    cur.commit()


    return jsonify({})
#-------------------------------------------------End Home----------------------------------------------------------------------------------------


#------------------------------------------------Start profile------------------------------------------------------------------------------------
@auth.route('/profile')
def profile():
    id = session['id']
    query1 = ("SELECT * FROM profile WHERE accounts_AccountID = %s")
    cursor = cur.cursor()
    cursor.execute(query1, (id, ))

    account = cursor.fetchone()
    name = account[5]
    gender = account[1]
    age = account[0]
    occupation = account[2]
    ethnicity = account[3]
    profilepic = account[4]
    #language = account[]


    gender_roommate = account[6]
    age_roommate = account[7]
    occupation_roommate = account[9]
    ethnicity_roommate = account[10]
    #language_roommate = account[]

    query2 = ("SELECT * FROM user_language WHERE accounts_AccountID = %s")
    cursor.execute(query2, (id, ))
    languageaccount = cursor.fetchone()
    language = languageaccount[0]

    query3 = ("SELECT * FROM roommate_language WHERE accounts_AccountID = %s")
    cursor.execute(query3, (id, ))
    language_roommateaccount = cursor.fetchone()
    if(language_roommateaccount):
        language_roommate = language_roommateaccount[0]
    else:
        language_roommate = 'None'


    return render_template('profile.html', Name2 = name, Age2 = age, name = name, gender = gender, age = age, occupation = occupation, ethnicity = ethnicity, language = language, gender_roommate = gender_roommate, age_roommate = age_roommate, occupation_roommate = occupation_roommate, ethnicity_roommate = ethnicity_roommate, language_roommate = language_roommate, profilepic = profilepic)

#-----------------------------------------------End Profile---------------------------------------------------------------------------------------


#-----------------------------------------------Start about------------------------------------------------------------------------------------
@auth.route('/about')
def about():
    return render_template("")
#-----------------------------------------------end about------------------------------------------------------------------------------------


@auth.route('/messages')
def messages():
    return render_template("messages.html")


#----------------------------------------------End Messages---------------------------------------------------------------------------------------

#---------------------------------------------Start Search/view Houses---------------------------------------------------------------------------------

# def abc(listOfStuff):
#     id = listOfStuff["_id"]
#     town = listOfStuff["bldg_contract_town"]
#     blk = listOfStuff["blk_no"]
#     maxFlr = listOfStuff["max_floor_lvl"]
#     yearCom = listOfStuff["year_completed"]
#     street = listOfStuff["street"]
#     market = listOfStuff["market_hawker"]
#     carpark = listOfStuff["multistorey_carpark"]

@auth.route('/search_house')
def search_house():
    
    return render_template("search_house.html")
# display short form town into full name
def convertToFullTown(town):
    if(town == 'AMK'):
        town = 'ANG MO KIO'
    elif (town == 'BB'):
        town = 'BUKIT BATOK'
    elif (town == 'BD'):
        town = 'BEDOK'
    elif (town == 'BH'):
        town = 'BISHAN'
    elif (town == 'BM'):
        town = 'BUKIT MERAH'
    elif (town == 'BP'):
        town = 'BUKIT PANJANG'
    elif (town == 'BT'):
        town = 'BUKIT TIMAH'
    elif (town == 'CCK'):
        town = 'CHOA CHU KANG'
    elif (town == 'CL'):
        town = 'CLEMENTI'
    elif (town == 'CT'):
        town = 'CENTRAL AREA'
    elif (town == 'GL'):
        town = 'GEYLANG'
    elif (town == 'HG'):
        town = 'HOUGANG'
    elif (town == 'JE'):
        town = 'JURONG EAST'
    elif (town == 'JW'):
        town = 'JURONG WEST'
    elif (town == 'KWN'):
        town = 'KALLANG/WHAMPOA'
    elif (town == 'MP'):
        town = 'MARINE PARADE'
    elif (town == 'PG'):
        town = 'PUNGGOL'
    elif (town == 'PRC'):
        town = 'PASIR RIS'
    elif (town == 'QT'):
        town = 'QUEENSTOWN'
    elif (town == 'SB'):
        town = 'SEMBAWANG'
    elif (town == 'SGN'):
        town = 'SERANGOON'
    elif (town == 'SK'):
        town = 'SENGKANG'
    elif (town == 'TAP'):
        town = 'TAMPINES'
    elif (town == 'TG'):
        town = 'TENGAH'
    elif (town == 'TP'):
        town = 'TOA PAYOH'
    elif (town == 'WL'):
        town = 'WOODLANDS'
    elif (town == 'YS'):
        town = 'YISHUN'
    return town
# get user search input, convert to short form
def convertToShortTown(input):
    if(input.upper() in 'ANG MO KIO'):
        input = 'AMK'
    elif (input.upper() in 'BUKIT BATOK'):
        input = 'BB'
    elif (input.upper() in 'BEDOK'):
        input = 'BD'
    elif (input.upper() in 'BISHAN'):
        input = 'BH'
    elif (input.upper() in 'BUKIT MERAH'):
        input = 'BM'
    elif (input.upper() in 'BUKIT PANJANG'):
        input = 'BP'
    elif (input.upper() in 'BUKIT TIMAH'):
        input = 'BT'
    elif (input.upper() in 'CHOA CHU KANG'):
        input = 'CCK'
    elif (input.upper() in 'CLEMENTI'):
        input = 'CL'
    elif (input.upper() in 'CENTRAL AREA'):
        input = 'CT'
    elif (input.upper() in 'GEYLANG'):
        input = 'GL'
    elif (input.upper() in 'HOUGANG'):
        input = 'HG'
    elif (input.upper() in 'JURONG EAST'):
        input = 'JE'
    elif (input.upper() in 'JURONG WEST'):
        input = 'JW'
    elif (input.upper() in 'KALLANG/WHAMPOA'):
        input = 'KWN'
    elif (input.upper() in 'MARINE PARADE'):
        input = 'MP'
    elif (input.upper() in 'PUNGGOL'):
        input = 'PG'
    elif (input.upper() in 'PASIR RIS'):
        input = 'PRC'
    elif (input.upper() in 'QUEENSTOWN'):
        input = 'QT'
    elif (input.upper() in 'SEMBAWANG'):
        input = 'SB'
    elif (input.upper() in 'SERANGOON'):
        input = 'SGN'
    elif (input.upper() in 'SENGKANG'):
        input = 'SK'
    elif (input.upper() in 'TAMPINES'):
        input = 'TAP'
    elif (input.upper() in 'TENGAH'):
        input = 'TG'
    elif (input.upper() in 'TOA PAYOH'):
        input = 'TP'
    elif (input.upper() in 'WOODLANDS'):
        input = 'WL'
    elif (input.upper() in 'YISHUN'):
        input = 'YS'
    return input
loopCount = 0
#get user inputs
def findHouse(query):
    # parameter= {'limit': 6, 'q' : query}
    parameter= {'q' : query}
    response = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=482bfa14-2977-4035-9c61-c85f871daf4e", params=parameter)
    #check if api can be accessed
    if(response.status_code != 200): 
        print("Error")
    searchList = response.json()
    # in list = help success result
    # in result = resource_id fields records _links limit total
    # formatted string Python JSON object 
    # print(json.dumps(response.json(), sort_keys=True, indent=4))
    listOfStuff = {}
    stuffList = searchList['result']['records']
    if(len(stuffList)==0):
        return 0
    # limit counter TBC?
    global loopCount
    loopCount = searchList['result']['total']
    listOfStuff = json.loads(json.dumps(stuffList, sort_keys=True))
    # print(json.dumps(stuffList, sort_keys=True, indent=4))
    return listOfStuff # = list of dictionary

@auth.route('/view_houses', methods = ['POST', 'GET']) # ‘/view_houses URL that triggered the result () function.
def view_houses():
    if request.method == 'POST':
        # result = request.form
        # getting input with name = fname in HTML form
        search = request.form.get("search")
        listOfStuff = findHouse(search)
        if(listOfStuff == 0):
            return render_template("view_houses.html", status = search, numOfResult = 0)

        townName = convertToFullTown(listOfStuff[0]['bldg_contract_town'])
        return render_template("view_houses.html", townName = townName, numOfResult = loopCount, slist = listOfStuff)

#--------------------------------------------End Search/view Houses------------------------------------------------------------------------------------

#---------------------------['GET', 'POST']----------------Start Update Roommate---------------------------------------------------------------------------------
@auth.route('/update_roommate', methods = ['GET', 'POST'])
def update_roommate():
    global user_profile_pic
    id = session['id']
    msg = ''
    query1 = ("SELECT * FROM profile WHERE accounts_AccountID = %s")
    #cur = mysql.connector.connect(user='root', password='2006project!', host='35.197.148.237', database='cz2006')
    cursor = cur.cursor()
    cursor.execute(query1, (id, ))

    account = cursor.fetchone()
    name = account[5]
    age = account[0]
    img_path = account[4]
    if request.method == 'POST':
        details = request.form
        roommate_gender = details['gender']
        roommate_age = details['roommate_age']
        roommate_occupation = details['roommate_occupation']
        roommate_ethnicity = details['roommate_ethnicity']
        roommate_language = details['roommate_lang']

        #cur = mysql.connector.connect(user='root', password='2006project!', host='35.197.148.237', database='cz2006')
        cursor = cur.cursor(buffered = True)

        query4 = ("SELECT * FROM profile WHERE accounts_AccountID = %s")
        cursor.execute(query4, (id, ))
        isthereinprofile = cursor.fetchone()

        query5 = ("SELECT * FROM roommate_language WHERE accounts_AccountID = %s")
        cursor.execute(query5, (id, ))
        isthereinroommatelang = cursor.fetchone()

        if(isthereinprofile):
            cursor.execute("UPDATE profile SET r_Gender = %s, r_Age = %s, r_Occupation = %s, r_Enthnicity = %s WHERE accounts_AccountID = %s", (roommate_gender, roommate_age, roommate_occupation, roommate_ethnicity, id, ))
            cur.commit()
        else:
            cursor.execute("INSERT INTO profile (r_Gender, r_Age, r_Occupation, r_Ethnicity, accounts_AccountID) VALUES (%s, %s, %s, %s, %s)", (roommate_gender, roommate_age, roommate_occupation, roommate_ethnicity, id,))
            cur.commit()
        if(isthereinroommatelang):
            cursor.execute("UPDATE roommate_language SET Language = %s WHERE accounts_AccountID = %s", (roommate_language, id, ))
            cur.commit()
        else:
            cursor.execute("INSERT INTO roommate_language (Language, accounts_AccountID) VALUES (%s, %s)", (roommate_language, id, ))
            cur.commit()
        
        msg = 'SUCCESSFULLY UPDATED!!'
        return redirect(url_for('auth.profile'))


    return render_template('update_roommate.html', msg = msg, Name = name, Age = age, profile_image = img_path)

#-------------------------, methods = []GET-, 'POST'-----------------End Update Roommate-----------------------------------------------------------------------------------

#-------------------------------------------Start Update Self--------------------------------------------------------------------------------------
@auth.route('/update_self', methods = ['GET', 'POST'])
def update_self():
    global user_age 
    global user_gender
    global user_occupation 
    global user_ethnicity 
    global user_language
    global user_name
    id = session['id']
    msg = ''
 
    cursor = cur.cursor(buffered = True)
    if request.method == 'POST':
        details = request.form
        name = details['name']
        age = details['age']
        occupation = details['Occupation']
        gender = details['selectgender']
        ethnicity = details['ethnicity']
        language_pref = details['language_preference']
        profile_pic = details['filename']
        
        cursor = cur.cursor(buffered = True)

        query4 = ("SELECT * FROM profile WHERE accounts_AccountID = %s")
        cursor.execute(query4, (id, ))
        isthere = cursor.fetchone()

        if(isthere):
            cursor.execute("UPDATE profile SET Age = %s, Occupation = %s, Ethnicity = %s, Name = %s, Gender = %s, profileImgPath=%s WHERE accounts_AccountID = %s", (age, occupation, ethnicity, name, gender, profile_pic, id, ))
            cur.commit()
            cursor.execute("UPDATE user_language SET Language = %s WHERE accounts_AccountID = %s", (language_pref, id, ))
            cur.commit()
        else:
            cursor.execute("INSERT INTO profile (Age, Occupation, Ethnicity, Name, Gender, accounts_AccountID, profileImgPath) VALUES (%s, %s, %s, %s, %s, %s, %s)", (age, occupation, ethnicity, name, gender, id, profile_pic, ))
            cur.commit()
            cursor.execute("INSERT INTO user_language (Language, accounts_AccountID) VALUES (%s, %s)", (language_pref, id, ))
            cur.commit()
        msg = 'SUCCESSFULLY UPDATED!!'
        return redirect(url_for('auth.profile'))
    
    return render_template('update_self.html', msg = msg, Name = user_name, Age = user_age, profile_image = user_profile_pic)

#--------------------------------------------End Update Self---------------------------------------------------------------------------------------

#--------------------------------------------Start Logout---------------------------------------------------------------------------------------

#--------------------------------------------End Update Self---------------------------------------------------------------------------------------

@auth.route('/404')
def other_page():
    return render_template("404.html")


@auth.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    current_account_id = 0
    user_name = ""
    user_age = ""
    user_gender = ""
    user_occupation  = ""
    user_ethnicity  = ""
    user_language = ""
    return redirect(url_for('auth.login'))
  
#--------------------------------------------End Logout---------------------------------------------------------------------------------------
