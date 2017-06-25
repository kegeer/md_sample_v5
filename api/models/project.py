from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .subproject import Subproject, SubprojectSchema
from .crud import CRUD

class Project(db.Model, CRUD):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(500))
    manager = db.Column(db.Integer)
    subprojects = db.relationship(
        'Subproject',
        backref='project',
        lazy='dynamic'
    )


    def __init__(self, name, subprojects=[]):
        self.name = name
        self.subprojects = subprojects

class ProjectSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Project
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    subprojects = fields.Nested(SubprojectSchema, many=True)
    # batches = fields.Nested(BatchSchema, many=True)
