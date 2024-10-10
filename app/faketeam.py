from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import TeamMember


def team(count):
    fake = Faker()
    i = 0
    while i < count:
        p = TeamMember(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            role=fake.job(),
            phone=fake.phone_number(),
            address=fake.address(),
            email=fake.email(),
            fb_social=fake.url(),
            x_social=fake.url(),
            lkdn_social=fake.url(),
            pin_social=fake.url(),
            about_me=fake.paragraph(nb_sentences=3),  # Using a paragraph instead of a long sentence
            image_url=fake.image_url()
        )
        db.session.add(p)
        try:
            db.session.commit()  # Commit each record, or batch commit if needed
            i += 1
        except IntegrityError:
            db.session.rollback()  # Rollback the session on error
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred: {e}")