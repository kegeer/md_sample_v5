from flask import request
from . import api
from api.models.user import User, UserSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/users', methods=['GET'])
def get_users():
    resource = User.query.all()
    user_schema = UserSchema(many=True)
    data = user_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/users', methods=['POST'])
def add_user():
    # fetched = request.get_json()
    # import json
    # return json.dumps(fetched)
    try:
        fetched = request.get_json()
        user_schema = UserSchema()
        user, error = user_schema.load(fetched)
        data = user_schema.dump(user.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    fetched = request.get_json()
    resource = User.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    user_schema = UserSchema()
    data = user_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    resource = User.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
