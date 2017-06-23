from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Subproject(db.Model):
    __tablename__ = 'subprojects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __init__(self, name, project_id=None):
        self.name = name
        self.project_id = project_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class SubprojectSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Subproject
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    project_id = fields.Integer()
