# Creators of SwipeMyRoommie
[Sankar Samiksha](https://github.com/S-Samiksha)

add in your names here 




Submitted to Nanyang Technological University (Singapore) on 1 Nov 2021

# How to use our code and get the website running 

## Pre-requsite
You have the following installed:
1. pip
2. python3
3. git 

## Installing Git

**If you are using ubuntu** <br>
~~~
$sudo apt-get install git-all
~~~

**If you are using windows** <br>

Download git from [here](https://gitforwindows.org/)

Follow the instructions from [here](https://github.com/git-guides/install-git#:~:text=To%20do%20so%2C%20Navigate%20to,installation%20by%20typing%3A%20git%20version%20)

**If you are using MacOS** <br>

Download git from [here](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect)

Follow the instructions from [here](https://github.com/git-guides/install-git#:~:text=To%20do%20so%2C%20Navigate%20to,installation%20by%20typing%3A%20git%20version%20)

**Check if you have downloaded git:**

Open command prompt/terminal 
~~~
> git --version 
~~~

## Clone Git Repository
Open command prompt / terminal (this instruction set follows Windows cmd prompt, this could vary if you are using another OS terminal)

~~~

> cd desktop

> git clone https://github.com/S-Samiksha/CX2006_Coding.git

> cd cx2006_coding

> pip install -r requirement.txt

~~~


## Installing MySql

From the following website download [mySql](https://dev.mysql.com/downloads/mysql/) 


After downloading MySql, creating a password, you will need to use it later. 

Set it as the following:
Username = `root` and password = `password` 



if you are using another username or password, open auth.py to change. <br>
cur = mysql.connector.connect(user='root', password='password',
                    host='localhost',
                    database='cz2006')

Change the password, user 
if needed change localhost (most likely do not need to)



## Setting up the database using mySQL command line client 
Now, do the following:
~~~
1. Open MySql Command Line Client 
2. Enter password 
3. Run the following commands:


mysql> DROP DATABASE cz2006;

mysql> CREATE DATABASE cz2006;

mysql> use cz2006;

mysql> source C:\Users\<user_name>\Desktop\cx2006_coding\db\cz2006_accounts.sql

mysql> source C:\Users\<user_name>\Desktop\cx2006_coding\db\cz2006_chat_data.sql

mysql> source C:\Users\<user_name>\Desktop\cx2006_coding\db\cz2006_profile.sql

mysql>  source C:\Users\<user_name>\Desktop\cx2006_coding\db\cz2006_roommate_language.sql

mysql>  source C:\Users\<user_name>\Desktop\cx2006_coding\db\cz2006_user_language.sql

~~~

Note: if you have stored the file cx2006_coding in a different folder, remember to change the pathfile accordingly<br>
<user_name> has to be changed to your own 

~~~
4. Close the SQL command client 

mysql> exit 
~~~


## Setting up the database using mySQL workbench 
Prerequisite: You are already connected to server <br>

Firstly, create a new schema called cz2006 (case sensitive). <br>

In the menu bar go to server --> data import --> select the `cx2006_coding/db` folder --> import 


## Running the python app

Go back into the command prompt/terminal 

make sure you are in the CX2006_coding folder

~~~
> python main.py 

OR 

> python3 main.py

~~~

This should generate the following ip address: `http://127.0.0.1:5000/`

Cope and paste into your web browser.

## Exiting 
~~~
press ctr + c to stop the server. 

> exit 

~~~










