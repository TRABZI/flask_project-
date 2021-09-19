# @Author : TRABZI Mohammed Amine 

from flask import Flask, render_template,request,session,redirect,url_for,g
import model
import os
app = Flask(__name__) # Declare flask application 

# app.secret_key=os.urandom(24)
# user=model.check_users

@app.route('/home',methods=['GET','POST'])
def homepage():
    return render_template('homepage.html')

@app.route('/login',methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('index.html',message='welcome')
    else:
        username=request.form['username'] 
        password=request.form['password']

        db_password=model.check_pw(username)
        # if username=='TRABZI' and password=='amine':
        if db_password!=None:
            if password==db_password[0]:
                # login_msg='Login Successful'
                msg=model.show_color(username)
                return render_template('foot.html',message=msg)
            else:
                error_msg='error!'
                return render_template('index.html',message=error_msg)
        else:
            error_msg='error!'
            return render_template('index.html',message=error_msg)


@app.route('/getfoot',methods=['GET','POST'])
def foot():
    return render_template('foot.html')


@app.route('/structur',methods=['GET'])
def func():
    return render_template('structur.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    msg='Please signe up !'
    if request.method=='GET':
        return render_template('signup.html',message=msg)
    else:
        username=request.form['username'] 
        password=request.form['passeword']
        favorit_color=request.form['favorit_color']
        msg=model.signup(username,password,favorit_color)
        return render_template('signup.html',message=msg)

if __name__ == '__main__':
    app.run(port=7000,debug=True)