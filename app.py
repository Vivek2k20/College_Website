'''
#################################################################
Importing stuff and initializing
#################################################################
'''
from flask import Flask,render_template,request,redirect,jsonify
import json,requests



app = Flask(__name__,template_folder = 'templates',static_folder='static')



'''
#################################################################
Home
#################################################################
'''
@app.route("/",methods=["GET","POST"])
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)