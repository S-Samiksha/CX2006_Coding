#main python 
#do not delete 

from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from Website import *


app = create_app()



if __name__ == '__main__':
    app.run(debug=True)


