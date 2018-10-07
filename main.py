from flask import Flask, request, redirect, render_template
import cgi
import re

match_username_password = re.compile(r"\w{3,20}\Z")
match_email = re.compile(r"\A\Z|\w+@\w+\.\w+")

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/welcome", methods=['GET'])
def welcome():
    username = request.args.get("username")
    return render_template('welcome.html', username=username)

@app.route("/", methods=['POST'])
def user_signup():

    error_bool = False
    username_err = ""
    password_err = ""
    vpassword_err = ""
    email_err = ""
    
    username = request.form['username']

    #if len(username) < 3 or len(username) > 20 or " " in username:
    if match_username_password.match(username) == None:
        error_bool = True
        username_err = 'Invalid username'

    password = request.form['password']

    #if len(password) < 3 or len(password) > 20 or " " in password:
    if match_username_password.match(password) == None:
        error_bool = True
        password_err = 'Invalid password'

    vpassword = request.form['vpassword']

    if vpassword != password:
        error_bool = True
        vpassword_err = 'Passwords do not match'

    email = request.form['email']

    #if len(email) == 0:
    #    pass
    #elif len(email) > 3 and len(email) < 20 and "@" in email and "." in email:
    #    pass
    #else:
    if match_email.match(email) == None:
        error_bool = True
        email_err = 'Invalid email'

    if error_bool:
        return render_template('signup.html', username=username, email=email, username_err=username_err, password_err=password_err, vpassword_err=vpassword_err, email_err=email_err)
    else:
        return redirect("/welcome?username=" + username)


@app.route("/", methods=['GET'])
def index():
    #encoded_error = request.args.get("error")
    return render_template('signup.html')

app.run()
