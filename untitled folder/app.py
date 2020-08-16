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


app = Flask(__name__)

app.config['DEBUG']=True
app.config['SECRET_KEY']= os.urandom(24)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def get_current_user():
    user_result = None
    if 'enrollment_ID' in session:
        enrollment_ID = session['enrollment_ID']
        db = get_db()
        cur = db.execute('select * from users where "enrollment_ID" = ?;',[enrollment_ID])
        user_result = cur.fetchone()
    return user_result


@app.route('/')
def home():
    return  render_template('first.html')

@app.route('/about')
def first():
    return  render_template('about-us.html')




@app.route('/dashboard')
def dashboard():
    user = get_current_user()
    if user:
        global parameters

        if  request.args.get('country') or request.args.get('category') or request.args.get('language'):
            parameters['country']=request.args.get('country')
            parameters['category']=request.args.get('category')
            parameters['language']=request.args.get('language')
            news_fetch = get_news(country=parameters['country'],category=parameters['category'],language=parameters['language'][-3:-1])
            return render_template('dashboard.html', user=user, params = parameters,news=news_fetch)
        # if request.args.get('source'):
        #     parameters['source']=request.args.get('source')
        #     # parameters=check_if_para_empty(parameters)
        #     news_fetch = get_news(country=parameters['country'],category=parameters['category'],source=parameters['source'])
        #     return render_template('dashboard.html', user=user, params = parameters,news=news_fetch)
        # if request.args.get('category'):
        #     parameters['category']=request.args.get('category')
        #     # parameters=check_if_para_empty(parameters)
        #     news_fetch = get_news(country=parameters['country'],category=parameters['category'],source=parameters['source'])
        #     return render_template('dashboard.html', user=user, params = parameters,news=news_fetch)
        news_fetch = get_news(country=parameters['country'],category=parameters['category'],source=parameters['source'])
        return render_template('dashboard.html', user=user, params = parameters,news=news_fetch)

    else :
        return redirect(url_for('login'))

@app.route('/mailsent')
def mailsent():
    user=get_current_user()
    email_(user['email'])
    return redirect(url_for('dashboard'))

@app.route('/login', methods = ['GET','POST'])
def login():
    user = get_current_user()
    if user:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form['login-username']
        password = hashlib.md5(request.form['login-password'].encode())
        db = get_db()
        cur = db.execute('select * from users where "enrollment_ID" = ?;',[username])
        result=cur.fetchone()
        if result:
            if result['password']==password.hexdigest() :
                session['enrollment_ID'] = username
                return  redirect(url_for('dashboard'))
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

@app.route('/logout')
def logout():
    user = get_current_user()
    if user:
        session.pop('enrollment_ID', None)
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/user_form')
def user_form_self():
    return render_template('user_form.html')

@app.route('/user_form_volunteer')
def user_form_vol():
    return render_template('user_form_volunteer.html')

@app.route('/volunteer_form')
def volunteer_form_reg():
    return render_template('volunteer_form.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if(__name__) == "__main__":
    app.run(host='0.0.0.0', port=5000)
