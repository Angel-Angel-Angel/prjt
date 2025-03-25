""" models """
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    address = db.Column(db.String(128), nullable=False)

    @classmethod
    def all(cls):
        return cls.query.all()
