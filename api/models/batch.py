from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields, post_load
from .sample import Sample, SampleSchema
from .crud import CRUD
from dateutil import parser as datetime_parser
from dateutil.tz import tzutc
from datetime import datetime

class Batch(db.Model, CRUD):
    __tablename__ = 'batches'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'))
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'))
    # 样本类型: 粪便, 脑脊液,DNA,土壤,发酵品,其他
    sample_type = db.Column(db.SmallInteger)
    # 样品状态, 到样状态(干冰保存,冰袋冻存,室温,异常)
    status = db.Column(db.SmallInteger)
    # 状态特征: 固态粪便,液体脑积液微黄
    character = db.Column(db.String(255))
    deliver_time = db.Column(db.DateTime, server_default=db.func.now())
    # deliver_time = db.Column(db.DateTime, default=datetime.now)
    arrive_time = db.Column(db.DateTime, server_default=db.func.now())
    express_num = db.Column(db.String(30), nullable=True)
    # 入库时间
    store_time = db.Column(db.DateTime, server_default=db.func.now())
    # 存储位置及温度
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'))
    # 所属项目
    subproject_id = db.Column(db.Integer, db.ForeignKey('subprojects.id'))
    # 技术路线
    roadmap_id = db.Column(db.Integer, db.ForeignKey('roadmaps.id'))
    # 备注, 异常情况
    remark = db.Column(db.Text, nullable=True)
    samples = db.relationship(
        'Sample',
        backref='batch',
        lazy='dynamic'
    )

    def __init__(self, agency_id, contact_id, sample_type, status, character, deliver_time, arrive_time, express_num, store_time, position_id, subproject_id, roadmap_id, remark, samples=[]):
        self.agency_id = agency_id
        self.contact_id = contact_id
        self.sample_type = sample_type
        self.status = status
        self.character = character
        # self.deliver_time = datetime_parser.parse(deliver_time).astimezone(
        #         tzutc()).replace(tzinfo=None)
        # self.arrive_time = datetime_parser.parse(arrive_time).astimezone(
        #         tzutc()).replace(tzinfo=None)
        self.deliver_time = deliver_time
        self.arrive_time = arrive_time
        self.express_num = express_num
        self.store_time = store_time
        self.position_id = position_id
        self.subproject_id = subproject_id
        self.roadmap_id = roadmap_id
        self.remark = remark
        self.samples = samples

class DateTiemSerializationField(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            return value
        else:
            if isinstance(value, datetime):
                return datetime_parser.parse(value).astimezone(tzutc()).replace(tzinfo=None)
            else:
                return None

class BatchSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Batch
        sqla_session = db.session
    id = fields.Integer(dump_only=True)
    agency_id = fields.Integer(required=True)
    contact_id = fields.Integer(required=True)
    sample_type = fields.Integer(required=True)
    status = fields.Integer(required=True)
    character = fields.String(required=True)
    deliver_time = fields.DateTime(required=True)
    arrive_time = fields.DateTime(required=True)
    # deliver_time = DateTiemSerializationField(attribute="deliver_time")
    # arrive_time = DateTiemSerializationField(attribute="arrive_time")
    express_num = fields.String(required=True)
    store_time = fields.DateTime(required=True)
    # store_time = DateTiemSerializationField(attribute="store_time")
    position_id = fields.Integer(required=True)
    subproject_id = fields.Integer(required=True)
    roadmap_id = fields.Integer(required=True)
    remark = fields.String(required=True)
    samples = fields.Nested(SampleSchema, many=True, only=['pmid', 'ori_num'])

    @post_load
    def make_batch(self, data):
        return Batch(**data)
