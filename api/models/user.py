from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .crud import CRUD
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import jwt
import os
from .role import Role, RoleSchema

role_users = db.Table('role_users', db.metadata,
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

class User(db.Model, CRUD):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(256))
    password = db.Column(db.String(256), nullable=False, unique=True)
    roles = db.relationship(
        'Role',
        secondary=role_users,
        backref='users'
    )

    def __init__(self, email, password, roles=[]):
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()
        for item in roles:
            role = Role.query.filter_by(slug=item).one()
            self.roles.append(role)

    def password_is_valid(self, password):
        return Bcrypt().check_password_hash(self.password, password)

    def generate_token(self, user_id):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=60),
                'iat': datetime.utcnow(),
                'sub': user_id
            }

            jwt_string = jwt.encode(
                payload,
                os.getenv('SECRET'),
                algorithm='HS256'
            )
            return jwt_string
        except Exception as e:
            return str(e)

    # def create_with_roles(self):
    #     if len(self.roles):
    #         for role in self.roles:
    #


    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, os.getenv('SECRET'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Token过期,请重新登录获取'
        except jwt.InvalidTokenError:
            return 'Token不合法,请登录或注册'



class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = db.session

    id = fields.Integer(dump_only=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    roles = fields.Nested(RoleSchema, many=True)
