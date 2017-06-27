from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .crud import CRUD

class Role(db.Model, CRUD):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    slug = db.Column(db.String(20))
    description = db.Column(db.String(255))

    def __init__(self, name, slug, description):
        self.name = name
        self.slug = slug
        self.description = description

class RoleSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Role
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    slug = fields.String(required=True)
    description = fields.String(required=True)
