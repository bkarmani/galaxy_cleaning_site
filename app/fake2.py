from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import Projects


def proj(count=30):
    fake = Faker()
    i=0
    while i < count:
        p=Projects(
            title = fake.sentence(nb_words=5),
            introduction=fake.text(),
            execution_title=fake.sentence(nb_words=5),
            execution_body=fake.text(),
            category='commercial cleaning',
            client = fake.name(),
            start=fake.past_date(),
            ended = fake.past_date(),
            problems_title=fake.sentence(nb_words=5),
            problems_body=fake.text(),
            solutions_title=fake.sentence(nb_words=5),
            solutions_body=fake.text(),
            total_projects=200
        )
        db.session.add(p)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()

