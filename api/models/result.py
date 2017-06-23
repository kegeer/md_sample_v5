from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 报告产出日期
    date = db.Column(db.DateTime, server_default=db.func.now())
    sample_id = db.Column(db.Integer, db.ForeignKey('samples.id'))
    # 结果状态: 未出具, 未审核, 已出具
    status = db.Column(db.SmallInteger, default = 0)
    # 审核员: 按理说是角色为审核员的人
    auditor = db.Column(db.String(10), nullable=True)
    auditor = db.Column(db.DateTime, nullable=True)
    content = db.Column(db.JSON)

    def __init__(self, date, sample_id, status, auditor, content):
        self.date = date
        self.sample_id = sample_id
        self.status = status
        self.auditor = auditor
        self.content = content

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class ResultSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Result
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    date = fields.DateTime(required=True)
    sample_id = fields.Integer()
    status = fields.Integer()
    auditor = fields.String()
    auditor_date = fields.DateTime()
    content = fields.String(required=True)
