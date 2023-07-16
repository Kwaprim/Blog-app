from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserSignUp(FlaskForm):
    
    username = StringField ("Username", validators = [DataRequired(), Length(min = 6, max = 25)])
    
    email = StringField ("Email", validators = [DataRequired(), Email()])
    
    userPassword = PasswordField ("Password", validators = [DataRequired(), Length(min = 6, max = 25)])
    
    confirmPassword = PasswordField ("Confirm Password", validators = [DataRequired(), EqualTo("userPassword")])
    
    submit = SubmitField("Sign Up")
    


class UserSignIn(FlaskForm):
    
    username = StringField("Username", validators = [DataRequired(), Length(min = 6, max = 25)])
    
    email = StringField("Email", validators = [DataRequired(), Email()])
    
    userPassword = PasswordField("Password", validators = [DataRequired(), Length(min = 6, max = 25)])
    
    rememberMe = BooleanField("Remember Me")
    
    submit = SubmitField("Login")
