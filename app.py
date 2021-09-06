'''
#################################################################
Importing stuff and initializing app
#################################################################
'''
from flask import Flask,render_template,request,redirect,jsonify
import json,requests



app = Flask(__name__,template_folder = 'templates',static_folder='static')



'''
#################################################################
Home Page
#################################################################
'''
@app.route("/",methods=["GET"])
def index():
    return render_template('home.html')






'''
#################################################################
Courses Page
#################################################################
'''
@app.route("/departments",methods=["GET"])
def departments():
    return render_template('departments.html')








'''
##################################################################
Launching App
##################################################################
'''
if __name__ == '__main__':
    app.run(debug=True)