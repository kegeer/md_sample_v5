from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .subproject import Subproject, SubprojectSchema

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    subprojects = db.relationship(
        'Subproject',
        backref='project',
        lazy='dynamic'
    )


    def __init__(self, name, subprojects=[]):
        self.name = name
        self.subprojects = subprojects

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class ProjectSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Project
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    subprojects = fields.Nested(SubprojectSchema, many=True)
    # batches = fields.Nested(BatchSchema, many=True)
