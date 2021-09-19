from flask import Flask, render_template, request,session,redirect,url_for,g
import model
import os

app = Flask(__name__) # Declare flask application 

app.secret_key=os.urandom(24)
db_users=model.check_users()

@app.before_request
def before_request():
    g.user=None
    if 'user' in session:
        user=[usr for usr in db_users if usr==session['user']][0]
        g.user = user

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)

        username=request.form['username'] 
        password=request.form['password']

        db_password=model.check_pw(username)
        if db_password!=None:
            if password==db_password[0]:  
                # return render_template('foot.html',message='welcome')
                session['user']=username
                return redirect(url_for('foot'))
            else:
                # return render_template('login.html',message='[login error]: Username or Password error')
                return redirect(url_for('login'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html',message='welcome')

@app.route('/foot',methods=['GET','POST'])
def foot():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('foot.html')

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