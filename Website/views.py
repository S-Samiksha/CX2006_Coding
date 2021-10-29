#do not delete 
#url end points 
#store standard routes 

from flask import Blueprint, render_template, url_for, redirect, request

views = Blueprint('views', __name__) #much easier to call the same as the file

@views.route('/')
#this is for the main page without logging in 
def main():
    return render_template("main.html")


@views.route('/about')
def about():
    return render_template("about.html")

