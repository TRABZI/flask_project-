# import code1
# code1.display("hello world")
# print(__name__)


from flask import Flask, render_template,request
import model

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('index.html',message='welcome')
    else:
        username=request.form['username'] 
        password=request.form['password']

        db_password=model.check_pw(username)
        # if username=='TRABZI' and password=='amine':
        if password==db_password:
            # login_msg='Login Successful'
            msg=model.show_color(username)
            return render_template('foot.html',message=msg)
        else:
            error_msg='error!'
            return render_template('index.html',message=error_msg)


@app.route('/GETfootball',methods=['GET','POST'])
def foot():
    return render_template('foot.html')


@app.route('/structur',methods=['GET','POST'])
def func():
    return render_template('structur.html')

if __name__ == '__main__':
    app.run(port=7000,debug=True)