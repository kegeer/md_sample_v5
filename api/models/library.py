from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .crud import CRUD

class Library(db.Model, CRUD):
    __tablename__ = 'libraries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

class LibrarySchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Library
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
