from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from sqlalchemy.orm import backref
from .contact import Contact, ContactSchema
from .batch import Batch, BatchSchema
from .crud import CRUD

class Agency(db.Model, CRUD):
    __tablename__ = 'agencies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    address = db.Column(db.Text)
    contacts = db.relationship(
        'Contact',
        backref=backref('agency', cascade='all, delete-orphan', single_parent=True),
        lazy='dynamic'
    )

    batches = db.relationship(
        'Batch',
        backref='agency',
        lazy='dynamic'
    )

    def __init__(self, name, address, contacts=[], batches=[]):
        self.name = name
        self.address = address
        self.contacts = contacts
        self.batches = batches


class AgencySchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Agency
        sqla_session = db.session
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    address = fields.String(required=True)
    contacts = fields.Nested(ContactSchema, many=True)
    batches = fields.Nested(BatchSchema, many=True)
