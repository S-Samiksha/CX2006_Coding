#initialize teh website folder as python package
#do not delete 

from flask import Flask 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Team_Alpha_CX2006' #does not matter what secret key this is 
    #encrypt and secure cookies and session data 
    #it does not matter because we are not doing a complete production level web development 

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app