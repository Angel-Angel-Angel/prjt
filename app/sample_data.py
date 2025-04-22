from .models import User
from . import db

def populate_sample_users():
    users = [
        User(name="John Mike", email="johnM@example.net", address="Union, NJ"),
        User(name="Angel Bello", email="Angel.Bello@example.com", address="Trenton, NJ"),
        User(name="Bob Kenny", email="bob.Kenny@example.org", address="Morris, NJ"),
        User(name="Crystal Sheer", email="Crystal.sheer@example.org", address="Middlesex, NJ"),
    ]
    db.session.add_all(users)
    db.session.commit()
