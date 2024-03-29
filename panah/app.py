from flask import Flask , render_template, g, request, url_for,redirect, session
import sqlite3
import requests
import json
import smtplib, ssl, glob
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from database import get_db
import hashlib
import requests
import os
from random import randint
from flask import Flask, render_template, request
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer


# bot = ChatBot("Candice")
# bot.set_trainer(ListTrainer)
# bot.train(['What is your name?', 'My name is Candice'])
# bot.train(['Who are you?', 'I am a bot' ])
# bot.train(['Who created you?', 'Tony Stark', 'Sahil Rajput', 'You?'])
# bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train("chatterbot.corpus.english")


app = Flask(__name__)

app.config['DEBUG']=True
app.config['SECRET_KEY']= os.urandom(24)




@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def get_current_user():
    user_result = None
    if 'login_ID' in session:
        enrollment_ID = session['login_ID']
        db = get_db()
        cur = db.execute('select * from login_users where "login_ID" = ?;',[enrollment_ID])
        user_result = cur.fetchone()
    return user_result


def init_db():
    db = get_db()
    with app.open_resource('sqldata.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.route('/')
def home():
    return  render_template('first.html')

@app.route('/about')
def first():
    return  render_template('about-us.html')

@app.route('/schemes_available')
def schemes_available():
    user = get_current_user()
    if user:
        schemes = []
        db = get_db()
        cur = db.execute('select "monthly","gender" from users where "phone" = ?;',[user['login_ID']])
        result=cur.fetchone()
        cur = db.execute('select * from schemes where "lowerbound">=? and "upperbound"<=?',[result['monthly'],result['monthly']])
        results = cur.fetchall()
        return render_template('schemes_available.html',schemes = results)
    else :
        return redirect(url_for('login'))

def getAllSchemes():
    db = get_db()
    cur = db.execute('select * from schemes')
    results = cur.fetchall()
    return results

@app.route('/volunteerTable')
def volunteerTable():
    
    user = get_current_user()
    if user:
        db = get_db()
        cur = db.execute('select * from users where isVolunteer=1' )
        result=cur.fetchall()
        return render_template('volunteerTable.html',volun = result)
    else :
        return redirect(url_for('login'))


@app.route('/dash')
def dash():
    schemes = getAllSchemes()
    return render_template('dashboard.html', schemes=schemes)

@app.route('/schemes')
def schemes():
    schemes = getAllSchemes()
    return render_template('schemes.html', schemes=schemes)

@app.route('/createScheme')
def createSchema():
    return render_template('createScheme.html')
@app.route('/mailsent')
def mailsent():
    user=get_current_user()
    email_(user['email'])
    return redirect(url_for('dashboard'))

@app.route('/login', methods = ['GET','POST'])
def login():
    user = get_current_user()
    if user:
        return redirect(url_for('dash'))
    if request.method == 'POST':
        username = request.form['login-username']
        password = request.form['login-password']
        db = get_db()
        cur = db.execute('select * from login_users where "login_ID" = ?;',[username])
        result=cur.fetchone()
        if result:
            if result['password']==password :
                session['login_ID'] = username
                return  redirect(url_for('dash'))
            else :
                return render_template('login.html',flag=0)
        else:
            return render_template('login.html',flag=0)
    return render_template('login.html',flag = 1)

@app.route('/signup', methods = ['GET','POST'])
def volunteer_form():
    if request.method == 'POST':
        name = request.form['signup-name']
        username = request.form['signup-username']
        email = request.form['signup-email']
        password = hashlib.md5(request.form['signup-password'].encode())
        token = hashlib.md5(str(randint(1,1000000)).encode())
        db = get_db() 
        cur = db.execute('select "id","name","username","email","password" from users where "username" = ?;',[username])
        result=cur.fetchone()
        if result:
            return render_template('signup.html',flag = 0)
        db.execute('insert into users ("name","username","email","password","token") values (?,?,?,?,?)',[name,username,email,password.hexdigest(),token.hexdigest()])
        db.commit()
        authenticator(username,token.hexdigest())

        return redirect(url_for('login'))
    return render_template('signup.html', flag = 1)


@app.route('/insertScheme', methods=['POST'])
def insertScheme():
    name = request.form['scheme_name']
    desc = request.form['desc']
    income_upper = request.form['income_upper']
    income_lower = request.form['income_lower']
    gender = request.form['gender']
    db = get_db()
    db.execute('insert into schemes ("name","description","lowerbound","upperbound","gender") values (?,?,?,?,?)',[name, desc, income_lower, income_upper,gender])
    db.commit()
    return redirect(url_for('dash'))

@app.route('/logout')
def logout():
    user = get_current_user()
    if user:
        session.pop('login_ID', None)
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/user_form', methods = ['GET','POST'])
def user_form_self():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        dob = request.form['dob']
        gender = request.form['gender']
        education = request.form['education']
        father = request.form['father']
        mother = request.form['mother']
        locality = request.form['locality']
        state = request.form['state']
        zip = request.form['zip']
        membersNum = request.form['membersNum']
        locality = request.form['locality']
        occupation = request.form["occupation"]
        monthly = request.form["income"]
        db = get_db()
        cur = db.execute('select * from users where "phone" = ?;',[mobile])
        result=cur.fetchone()
        db.execute('insert into users ("name","phone","father","mother","dob","gender","email","education","address","fam","password") values (?,?,?,?,?,?,?,?,?,?,?)',[name,mobile,father,mother,dob,gender,email,education,locality,membersNum,password])
        db.execute('insert into login_users ("login_ID","password") values (?,?)',[mobile,password])
        db.commit()
        return redirect(url_for('home'))
    return render_template('user_form.html')

@app.route("/temp")
def temp():
    return render_template("DashboardVolunteer.html")
@app.route('/user_form_volunteer', methods = ['GET','POST'])
def user_form_vol():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        password = hashlib.md5(password.encode())
        password = password.hexdigest()
        mobile = request.form['phone']
        email = request.form['email']
        dob = request.form['dob']
        gender = request.form['gender']
        education = request.form['education']
        father = request.form['father']
        mother = request.form['mother']
        locality = request.form['locality']
        state = request.form['state']
        zip = request.form['zip']
        membersNum = request.form['membersNum']
        locality = request.form['locality']
        vol_id = request.form['volunteer']
        documents = request.form['documents']
        occupation = request.form["occupation"]
        monthly = request.form["income"]
        db = get_db()
        cur = db.execute('select * from users where "phone" = ?;',[mobile])
        result=cur.fetchone()
        if result:
            return render_template('user_form.html',flag = 0)
        db.execute('insert into users ("name","phone","father","mother","dob","gender","email","education","address","fam","password","volunteer_id", "documents","monthly","occupation") values (?,?,?,?,?,?,?,?,?,?,?,?,?)',[name,mobile,father,mother,dob,gender,email,education,locality,membersNum,password,vol_id, documents,monthly,occupation])
        db.commit()
        return redirect(url_for('home'))
    return render_template('user_form_volunteer.html')

@app.route('/volunteer_form', methods = ['GET','POST'])
def volunteer_form_reg():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        dob = request.form['dob']
        gender = request.form['gender']
        education = request.form['education']
        father = request.form['father']
        mother = request.form['mother']
        locality = request.form['locality']
        state = request.form['state']
        zip = request.form['zip']
        locality = request.form['locality']
        db = get_db()
        cur = db.execute('select * from volunteers where "phone" = ?;',[mobile])
        result=cur.fetchone()
        if result:
            return render_template('user_form.html',flag = 0)
        db.execute('insert into users ("name","phone","father","mother","dob","gender","email","education","address","isVolunteer") values (?,?,?,?,?,?,?,?,?,1)',[name,mobile,father,mother,dob,gender,email,education,locality])
        db.commit()
        return redirect(url_for('home'))

    return render_template('volunteer_form.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if(__name__) == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
