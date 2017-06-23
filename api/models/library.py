from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Library(db.Model):
    __tablename__ = 'libraries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class LibrarySchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Library
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
