import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    # Here we're associating the DB column names to the variables we'll use. 
    id = db.Column(db.Integer, primary_key=True)   # could be using a UUID here...
    username = db.Column(db.String(80)) # limits size to 80 characters
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()