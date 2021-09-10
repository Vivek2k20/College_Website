'''
#################################################################
Importing stuff and initializing app
#################################################################
'''
from flask import Flask,render_template,request,g,session,url_for
import sqlite3
from werkzeug.utils import redirect



app = Flask(__name__,template_folder = 'templates',static_folder='static')
app.config['SECRET_KEY'] = "@\xec\xf7\t6\xe9mVc8\x1a\xaa\xa2\xf2``TT\xb1SU\xf8\x14W"









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




def CurrentAccent():
    try:
        if session['theme']:
            return session['theme']
    except:
        session['theme']="red"
        return session['theme']

def SetAccent(accent):
    if(accent=="red" or accent=="orange" or accent=="green" or accent=="yellow" or accent=="purple"):
        session['theme']=accent
        return
    else:
        try:
            if session['theme']:
                return
        except:
            session['theme']="red"
            return







'''
#################################################################
Theme Handling
#################################################################
'''
@app.route("/theme/<accent>",methods=["GET"])
def settheme(accent):
    SetAccent(accent)
    try:
        if session['url']:
            return redirect(session['url'])
    except:
        return redirect(url_for('index'),theme=CurrentAccent())




'''
#################################################################
Home Page
#################################################################
'''
@app.route("/",methods=["GET"])
def index():
    session['url'] = url_for('index')
    return render_template('home.html',theme=CurrentAccent())






'''
#################################################################
Departments Page
#################################################################
'''
@app.route("/departments",methods=["GET"])
def departments():
    session['url'] = url_for('departments')
    return render_template('departments.html',theme=CurrentAccent())










'''
#################################################################
Facilities Page
#################################################################
'''
@app.route("/facilities",methods=["GET"])
def facilities():
    session['url'] = url_for('facilities')
    return render_template('facilities.html',theme=CurrentAccent())











'''
#################################################################
Clubs Page
#################################################################
'''
@app.route("/clubs",methods=["GET"])
def clubs():
    session['url'] = url_for('clubs')
    return render_template('clubs.html',theme=CurrentAccent())











'''
#################################################################
Contact Us Page
#################################################################
'''
@app.route("/contactus",methods=["GET","POST"])
def contactus():
    if request.method=="GET":
        session['url'] = url_for('contactus')
        return render_template('contactus.html',msg="",theme=CurrentAccent())
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
        return render_template('contactus.html',msg=msg1,theme=CurrentAccent())








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
    from waitress import serve
    serve(app)
