#do not delete 
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__) #much easier to call the same as the file


@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/register')
def register():
    return render_template("register.html")

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/profile')
def profile():
    return render_template("profile.html")

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