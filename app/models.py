from . import db
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app
from .helpers import slugify



# user model
class User(db.Model, UserMixin):
    __table_name__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(40), unique=True, index=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    registered = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    password_hash = db.Column(db.String(150))
    posts =  db.relationship(
        'Post',
        order_by='Post.created.desc()',
        passive_updates=False,
        cascade='all,delete-orphan',
        backref='author',
    )


    @property
    def password(self):
        raise AttributeError('password object is not a visible field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
     #email confirmation token generation functions
     
    def generate_confirmation_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'confirm':self.id})
    
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True


    def __repr__(self):
        return(self.username)
    

from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

class Post(db.Model):
    PER_PAGE = 5

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(256), nullable=False)
    markup = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False, unique=True)

    #images and video fields
    image_url = db.Column(db.String(255), nullable=True)  # To store image URL or path
    image_alt_text = db.Column(db.String(255), nullable=True)  # Alt text for accessibility
    video_url = db.Column(db.String(255), nullable=True)  # To store video URL or path
    video_caption = db.Column(db.String(255), nullable=True)  # Optional caption for videos

    author_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
    )
    visible = db.Column(db.Boolean, default=False)

    def __init__(self, title, markup, author_id, visible):
        self.created = datetime.now(timezone.utc)
        self.updated = self.created
        self.title = title
        self.markup = markup
        self.slug = slugify(self.created, title)
        self.author_id = author_id
        self.visible = visible

    def __repr__(self):
        return u'<Post(%s,%s,%s)>' % (self.id, self.slug, self.author.name)

    def update(self, title, markup, visible):
        """Update post values.

        Handles title slug and last update tracking.

        """
        self.updated = datetime.now(timezone.utc)
        self.title = title
        self.markup = markup
        self.slug = slugify(self.created, title)
        self.visible = visible

    @property
    def is_updated(self):
        """Validate if this post has been updated since created."""
        return self.updated > self.created
    

class Projects(db.Model):
    __table_name__ = 'projects'
    id = db.Column(db.Integer(), primary_key=True)
    number_of_projects = db.Column(db.Integer(), unique=True, nullable=False)


    def __repr__(self):
        return f'number of projects: {self.number_of_projects}'



class CartItem(db.Model):
    __table_name__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)    

class Categories(db.Model):
    __table_name__ = 'categories'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True)

    def __repr__(self):
        return f'{self.name}'


class Products(db.Model):
    __table_name__ ='products'
    id = db.Column(db.Integer(), primary_key=True)
    product_name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image1 = db.Column(db.String(200), nullable=False)
    image2 = db.Column(db.String(200), nullable=False)
    image3 = db.Column(db.String(200), nullable=False)
    image4 = db.Column(db.String(200), nullable=False)
    old_price = db.Column(db.String(10), nullable=False)
    price = db.Column(db.String(10), nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'))
    
    


    def __repr__(self):
        return f'{self.product_name}'








    




    

