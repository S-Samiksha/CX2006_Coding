#initialize teh website folder as python package
#do not delete 

from flask import Flask 
from flask_mysqldb import MySQL
from .views import views
from .auth import auth

app = Flask(__name__)
mysql=MySQL(app)


def create_app():
    app.config['SECRET_KEY'] = 'Team_Alpha_CX2006'
    app.config['MYSQL_HOST']='localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'password' #this might change from person to person
    app.config['MYSQL_DB']= 'cz2006'
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app