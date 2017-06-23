from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .crud import CRUD

class Contact(db.Model, CRUD):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(20))
    agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'))

    def __init__(self, name, phone, email, agency_id=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.agency_id = agency_id

class ContactSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Contact
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    phone = fields.String(required=True)
    email = fields.String(required=True)
    agency_id = fields.Integer()
