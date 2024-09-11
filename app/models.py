from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app

class User(db.Model, UserMixin):
    __table_name__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(40), unique=True, index=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    password_hash = db.Column(db.String(150))
    cart_items = db.relationship('CartItem', backref='user', lazy=True)


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

    products = db.relationship('Products', back_populates='category')

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
    
    category = db.relationship('Categories', back_populates='products')


    def __repr__(self):
        return f'{self.product_name}'


class Subscribers(db.Model):
    __table_name__ = 'subscribers'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(65), unique=True, nullable=False)


    

