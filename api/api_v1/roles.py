from flask import request
from . import api
from api.models.role import Role, RoleSchema
from api.models.user import User
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/roles', methods=['GET'])
def get_roles():
    resource = Role.query.all()
    role_schema = RoleSchema(many=True)
    data = role_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/roles', methods=['POST'])
def add_role():
    try:
        fetched = request.get_json()
        role_schema = RoleSchema()
        role, error = role_schema.load(fetched)
        data = role_schema.dump(role.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/roles/<int:id>', methods=['PUT'])
def update_role(id):
    fetched = request.get_json()
    resource = Role.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    role_schema = RoleSchema()
    data = role_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/roles/<int:id>', methods=['DELETE'])
def delete_role(id):
    resource = Role.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)

@api.route('/users/<int:id>/roles', methods=['GET'])
def get_user_roles(id):
    resource = User.query.get_or_404(id)
    role_schema = RoleSchema()
    data = role_schema.dump(resource.roles).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })
