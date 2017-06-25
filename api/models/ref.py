from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .crud import CRUD

class Ref(db.Model, CRUD):
    __tablename__ = 'refs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    info_id = db.Column(db.Integer, db.ForeignKey('infos.id'))
    status = db.Column(db.SmallInteger)
    color = db.Column(db.SmallInteger)
    img = db.Column(db.SmallInteger)
    desc = db.Column(db.Text)

    def __init__(self, info_id, status, color, img, desc):
        self.info_id = info_id
        self.status = status
        self.color = color
        self.img = img
        self.desc = desc


class RefSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Ref
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    info_id = fields.Integer()
    status = fields.Integer(required=True)
    color = fields.Integer(required=True)
    img = fields.Integer(required=True)
    desc = fields.String(required=True)
