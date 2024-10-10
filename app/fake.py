from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User, Post
from datetime import datetime


def users():
  fake = Faker()
  u = User(email='support@galaxycleaning.co.uk',
  username='Support',
  password='PA33word',
  name='Patrick poll',
  location='United Kingdom',
  about_me='As a dedicated professional in the cleaning services industry for several years, I have built my career on the commitment to creating clean and welcoming spaces for my clients. My experience has allowed me to hone my skills and develop a reputation for delivering exceptional cleaning services. I focus on quality and customer satisfaction, whether it’s residential cleaning, commercial spaces, or specialized services. My passion for cleanliness drives me to go above and beyond in every task, ensuring that my clients receive the best possible experience.',
  member_since=datetime.now())
  db.session.add(u)
  print('okay success')
  db.session.commit()
  print('done')


def posts(count=100):
 fake = Faker()
 for i in range(count):
    u = User.query.first()
    p = Post(body=fake.text(),
    timestamp=fake.past_date(),
    title=fake.sentence(nb_words=4),
    author=u)
    db.session.add(p)
    db.session.commit()