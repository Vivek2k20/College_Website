'''
#################################################################
Importing stuff and initializing app
#################################################################
'''
from flask import Flask,render_template,request,g
import sqlite3



app = Flask(__name__,template_folder = 'templates',static_folder='static')










""""
########################################
CONNECTION TO DATABASE (FUNCTIONS)
########################################
"""
def connect_db():
    return sqlite3.connect('feedback.db')


@app.before_request
def before_request():
    g.db = connect_db()


"""
########################################
########################################
"""








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
Departments Page
#################################################################
'''
@app.route("/departments",methods=["GET"])
def departments():
    return render_template('departments.html')










'''
#################################################################
Facilities Page
#################################################################
'''
@app.route("/facilities",methods=["GET"])
def facilities():
    return render_template('facilities.html')











'''
#################################################################
Clubs Page
#################################################################
'''
@app.route("/clubs",methods=["GET"])
def clubs():
    return render_template('clubs.html')











'''
#################################################################
Contact Us Page
#################################################################
'''
@app.route("/contactus",methods=["GET","POST"])
def contactus():
    if request.method=="GET":
        return render_template('contactus.html',msg="")
    else:
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        comment=request.form['comment']
        g.db=connect_db()
        try:
            g.db.execute("INSERT INTO Contact (Name,Email,Phone,Comment) VALUES(?,?,?,?);",[name,email,phone,comment])
            g.db.commit()
            g.db.close()
        except:
            g.db.rollback()
            g.db.close()
        msg1="Thank you for contacting us,"+request.form['name']+'!'
        return render_template('contactus.html',msg=msg1)








'''
##################################################################
Launching App
##################################################################
'''
if __name__ == '__main__':
    with app.app_context():
        before_request()
        try:
            g.db.execute("DROP TABLE IF EXISTS Contact;")
            g.db.execute("CREATE TABLE IF NOT EXISTS Contact(ID integer PRIMARY KEY,Name text NOT NULL,Email text NOT NULL,Phone numeric NOT NULL,Comment text NOT NULL);")
            g.db.commit()
            g.db.close()
        except:
            g.db.rollback()
            g.db.close()
    app.run(debug=True)

