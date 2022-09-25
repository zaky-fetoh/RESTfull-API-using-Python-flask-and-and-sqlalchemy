from . import datebase
import marshmallow as ma 
import marshmallow_sqlalchemy as masql

db = datebase.db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    def create(self):
        db.session.add(self)
        db.session.commit()
        return db
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self


class AuthorSchema(masql.SQLAlchemySchema):
    class Meta(masql.SQLAlchemySchema.Meta):
        model= Author
        sqla = db.session
    id= ma.fields.Number()
    first_name = ma.fields.String(required= True)
    last_name= ma.fields.String(required= True)



