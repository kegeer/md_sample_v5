from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .result import Result, ResultSchema
from .crud import CRUD

class Sample(db.Model, CRUD):
    __tablename__ = 'samples'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    pmid = db.Column(db.String(20))
    ori_num = db.Column(db.String(20))
    # 与下面的amount配合,标识是重量还是体积
    type = db.Column(db.SmallInteger, nullable=True)
    # 样品量,体积或重量(ml/g)
    amount = db.Column(db.Float, nullable=True)
    # 测序类型
    sequence_method = db.Column(db.SmallInteger, nullable=True)
    primer = db.Column(db.SmallInteger, nullable=True)
    sequencer = db.Column(db.SmallInteger, nullable=True)
    # 文库编号
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'))
    # 备注, 异常情况
    remark = db.Column(db.Text, nullable=True)
    results = db.relationship(
        'Result',
        backref='sample',
        lazy='dynamic'
    )

    def __init__(self, batch_id, client_id, pmid, ori_num, type, amount, sequence_method, primer, sequencer, library_id, remark, results=[]):
        self.batch_id = batch_id
        self.client_id = client_id
        self.pmid = pmid
        self.ori_num = ori_num
        self.type = type
        self.amount = amount
        self.sequence_method = sequence_method
        self.primer = primer
        self.sequencer = sequencer
        self.library_id = library_id
        self.remark = remark
        self.results = results
        # self.batches = batches

class SampleSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Sample
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    batch_id = fields.String(required=True)
    client_id = fields.Integer()
    pmid = fields.String(required=True)
    ori_num = fields.String(required=True)
    type = fields.Integer(required=True)
    amount = fields.Float(required=True)
    sequence_method = fields.String(required=True)
    primer = fields.Integer()
    sequencer = fields.Integer()
    library_id = fields.Integer()
    remark = fields.String()
    results = fields.Nested(ResultSchema, many=True)
