from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .crud import CRUD

class Category(db.Model, CRUD):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name, infos=[]):
        self.name = name

class CategorySchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Category
        sqla_session = db.session
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
