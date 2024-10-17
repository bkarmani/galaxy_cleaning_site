from . import db, login_manager
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app, url_for
from markdown import markdown
import hashlib
import  bleach
from app.exceptions import ValidationError




class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.now(timezone.utc))
    last_seen = db.Column(db.DateTime(), default=datetime.now(timezone.utc))
    posts = db.relationship('Post', backref='author', cascade='all, delete-orphan', lazy='dynamic')
    

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = User.query.get(data.get('reset'))
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps(
            {'change_email': self.id, 'new_email': new_email}).decode('utf-8')

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        self.avatar_hash = self.gravatar_hash()
        db.session.add(self)
        return True

    def ping(self):
        self.last_seen = datetime.now(timezone.utc)
        db.session.add(self)


    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return f'{self.username}'



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now(timezone.utc))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return f'post: {self.id}' 


class Projects(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer(), primary_key=True)
    
    # Project details
    title = db.Column(db.String(150), nullable=False)  # Title of the project
    introduction = db.Column(db.Text(), nullable=False)  # Introduction of the project

    category = db.Column(db.String(150))
    client = db.Column(db.String(50))
    start = db.Column(db.DateTime, index=True, default=datetime.now(timezone.utc))
    ended = db.Column(db.DateTime, index=True, default=datetime.now(timezone.utc))
    # Execution details
    execution_title = db.Column(db.String(150), nullable=False)  # Title of how you carried out the project
    execution_body = db.Column(db.Text(), nullable=False)  # Body explaining how you carried out the project
    
    # Problems encountered
    problems_title = db.Column(db.String(150), nullable=False)  # Title of the problems encountered
    problems_body = db.Column(db.Text(), nullable=False)  # Body explaining the problems encountered
    
    # Solutions applied
    solutions_title = db.Column(db.String(150), nullable=False)  # Title of the solutions applied
    solutions_body = db.Column(db.Text(), nullable=False)  # Body explaining the solutions applied
    
    total_projects = db.Column(db.Integer(), default=150)  # You can edit this value manually
    image1_url = db.Column(db.String(255))
    image2_url = db.Column(db.String(255))
    def __repr__(self):
        return f'<Project {self.title}>'
    



class TeamMember(db.Model):
    __tablename__ = 'team_member'
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(65), nullable=False)
    last_name = db.Column(db.String(65), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(15),unique=True, nullable=False)
    address = db.Column(db.Text(), nullable=False)
    email = db.Column(db.String(64), unique=True, index=True)
    fb_social =db.Column(db.String(120), unique=True)
    x_social =db.Column(db.String(120), unique=True)
    lkdn_social =db.Column(db.String(120), unique=True)
    pin_social =db.Column(db.String(120), unique=True)
    about_me = db.Column(db.Text(), nullable=False)
    image_url = db.Column(db.String(255))


    def __repr__(self):
        return f'Team{self.email}'


class Subscribers(db.Model):
    __table_name__ = 'subscribers'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return self.email
    

    




    




    

