#main python 
#do not delete 

from Website import create_app
#when we put the __init__.py it makes the Website folder a python package so we can import it as a python package

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
#what this above line does is it only runs the debug file if and only if we run the main.py file

#this python file is where you start 


##How to run this file ------------------------
### ctr shift p --> python: select interpreted --> select recommended python version
### ctr alt N to run the file 
### you will get the local host 

