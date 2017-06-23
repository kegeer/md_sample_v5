from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .sample import Sample, SampleSchema

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    gender = db.Column(db.SmallInteger(), nullable=True)
    age = db.Column(db.SmallInteger(), nullable=True)
    height = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    # 额外信息,包括各项指标
    extra = db.Column(db.JSON(), nullable=True)
    samples = db.relationship(
        'Sample',
        backref='client',
        lazy='dynamic'
    )


    def __init__(self, name, gender, age, height, weight, extra, samples=[]):
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.extra = extra
        self.samples = samples

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class ClientSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Client
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    gender = fields.Integer()
    age = fields.Integer()
    height = fields.Float()
    weight = fields.Float()
    extra = fields.String()
    samples = fields.Nested(SampleSchema, many=True)
