""" the data """
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # Add sample users
    user1 = User(name="John Mike", email="johnM@example.net", address="Union, NJ")
    user2 = User(name="Angel Bello", email="Angel.Bello@example.com", address="Trenton, NJ")
    user3 = User(name="Bob Kenny", email="bob.Kenny@example.org", address="Morris, NJ")
    user4 = User(name="Crystal Sheer", email="Crystal.sheer@example.org", address="Middlesex, NJ")

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.commit()
