from dataclasses import dataclass
from sqlite3 import DatabaseError
from . import datebase

db = datebase.db


class book(db.Model):
    id = db.Column(db.Integer)
    name = db.Column(db.String(30))
    author_id = db.Column(db.Integer)

    def __init__(self, name, author_id):
        self.author_id = author_id
        self.name = name

    def save(self):
        db.session.add(self)
        db.commit(self)
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

