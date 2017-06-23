from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Contract(db.Model):
    __tablename__ = 'contracts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subproject_id = db.Column(db.Integer, db.ForeignKey('subprojects.id'))
    name = db.Column(db.String(255))
    sign_date = db.Column(db.DateTime)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    region = db.Column(db.String(255))
    agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'))
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'))
    product_type = db.Column(db.String(100))
    sequence_area = db.Column(db.String(100))
    sequence_type = db.Column(db.String(100))
    data_size = db.Column(db.String(100))

    def __init__(self, name, sign_date, start_date, end_date, region, product_type, sequence_area, sequence_type, data_size, subproject_id=None, agency_id=None, contact_id=None):
        self.subproject_id = subproject_id
        self.name = name
        self.sign_date = sign_date
        self.start_date = start_date
        self.end_date = end_date
        self.region = region
        self.agency_id = agency_id
        self.contact_id = contact_id
        self.product_type = product_type
        self.sequence_area = sequence_area
        self.sequence_type = sequence_type
        self.data_size = data_size

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class ContractSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Contract
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    subproject_id = fields.Integer()
    name = fields.String(required=True)
    sign_date = fields.DateTime(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
    region = fields.String(required=True)
    agency_id = fields.Integer()
    contact_id = fields.Integer()
    product_type = fields.String()
    sequence_area = fields.String()
    sequence_type = fields.String()
    data_size = fields.String()
