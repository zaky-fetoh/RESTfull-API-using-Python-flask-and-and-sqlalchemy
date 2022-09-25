from . import datebase
import marshmallow as ma
import marshmallow_sqlalchemy as masql


db = datebase.db


class Book(db.Model):
    id = db.Column(db.Integer,primary_key =True)
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


class BookSchema(masql.SQLAlchemySchema):
    class Meta(masql.SQLAlchemySchema.Meta):
        model = Book
        sqla = db.session

    id = ma.fields.Number()
    name = ma.fields.String(required= True)
    author_id = ma.fields.String(required= True)
