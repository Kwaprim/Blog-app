from firstapp.models import User, Post
from flask import render_template, url_for, flash, redirect
from firstapp.user_forms import UserSignUp, UserSignIn
from firstapp import app

posts = [
        {
        "author": "Prince Millidah",
        "title": "Coding",
        "content": "Programming is hard but I will make it through and land an internship",
        "date": "July 05, 2023"
        }
        ]

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("home.html", posts = posts)


@app.route("/about")
def aboutpage():
    return render_template("about.html", title = "About")


@app.route("/signup")
def signuppage():
    form = UserSignUp()
    
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("homepage"))
    
    return render_template("signup.html", title = "Sign Up", form = form)

@app.route("/signin")
def signinpage():
    form = UserSignIn()
    
    if form.validate_on_submit():
        flash(f"Login Successful!", "success")
        return redirect(url_for("homepage"))
    
    return render_template("signin.html", title = "Sign Up", form = form)
