from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name, infos=[]):
        self.name = name

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class CategorySchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Category
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
