import datetime
from itsdangerous import URLSafeTimedSerializer as Serializer
from flaskblog import db, login_manager
from flask import current_app
from flask_login import UserMixin
import secrets


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def get_reset_token(self, expires_sec=300):
        token = secrets.token_urlsafe(32)  # Generates a URL-safe token with 32 bytes of randomness
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_sec)
        return token, expiration_time
   
    @staticmethod # static method does not take self as an argument
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)  # Try to load the token
            user_id = data['user_id']
            expiration_time = data.get('expiration_time') # try to load the token
        except:
            return None
        
        if expiration_time is not None and datetime.datetime.utcnow() > expiration_time:
            return None
        
        return User.query.get(user_id) # return the user id if the token is valid

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"