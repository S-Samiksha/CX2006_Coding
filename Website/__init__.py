#initialize teh website folder as python package
#do not delete 
#do not edit 
#do not touch 

from flask import Flask 
from .views import views
from .auth import auth

app = Flask(__name__)


def create_app():
    app.config['SECRET_KEY'] = 'Team_Alpha_CX2006'
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app