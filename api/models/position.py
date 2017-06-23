from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Position(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    position = db.Column(db.String(100))
    tempr = db.Column(db.String(100))

    def __init__(self, position, tempr):
        self.position = position
        self.tempr = tempr

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class PositionSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Position
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    position = fields.String(required=True)
    tempr = fields.String(required=True)
