from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    year = db.Column(db.Date)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __init__(self,title, year, author_id=None):
        self.title = title
        self.year = year
        self.author_id = author_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class BookSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Book
        sqla_session = db.session

    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    title = fields.String(dump_to=True)
    author_id = fields.Integer()
