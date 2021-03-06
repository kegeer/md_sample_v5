from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .ref import Ref, RefSchema
from .category import Category, CategorySchema
from .crud import CRUD

category_infos = db.Table('category_infos', db.metadata,
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')),
    db.Column('info_id', db.Integer, db.ForeignKey('infos.id'))
)

class Info(db.Model, CRUD):
    __tablename__ = 'infos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(255), nullable=True)
    e_name = db.Column(db.String(255), nullable=True)
    # TODO 类型信息,暂时还不确定是否和category有区别
    desc = db.Column(db.String(255), nullable=True)
    ref_min = db.Column(db.Float, nullable=True)
    ref_max = db.Column(db.Float, nullable=True)
    alias = db.Column(db.String(50), nullable=True)
    refs = db.relationship(
        'Ref',
        backref='info',
        lazy='dynamic'
    )
    categories = db.relationship(
        'Category',
        secondary=category_infos,
        backref='infos'
    )

    def __init__(self, c_name, e_name, desc, ref_min, ref_max, alias, refs=[], categories=[]):
        self.c_name = c_name
        self.e_name = e_name
        self.desc = desc
        self.ref_min = ref_min
        self.ref_max = ref_max
        self.alias = alias
        self.refs = refs
        self.categories = categories


class InfoSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Info
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    c_name = fields.String(required=True)
    e_name = fields.String(required=True)
    desc = fields.String(required=True)
    ref_min = fields.String(required=True)
    ref_max = fields.String(required=True)
    alias = fields.String(required=True)
    refs = fields.Nested(RefSchema, many=True)
    categories = fields.Nested(CategorySchema, many=True)
    # batches = fields.Nested(BatchSchema, many=True)
