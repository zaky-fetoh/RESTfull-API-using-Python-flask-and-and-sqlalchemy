from . import datebase
import marshmallow as ma 
import marshmallow_sqlalchemy as masql

db = datebase.db

class Author(db.Model):
    id = db.Column(db.Integer)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))

    def __init__(self, firt_name, last_name) -> None:
        self.first_name = firt_name
        self.last_name = last_name
    def create(self):
        db.session.add(self)
        db.session.commit()
        return db
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self


class AuthorSchema(masql.ModelSchema):
    class Meta(masql.ModelSchema.Meta):
        model= Author
        sqla = db.session
    id= ma.fields.Number()
    first_name = ma.fields.String()
    last_name= ma.fields.String()



