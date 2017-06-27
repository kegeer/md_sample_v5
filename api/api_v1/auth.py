from flask import request
from . import api
from api.utils.response import response_with
from api.models.user import User, UserSchema
import api.utils.response as resp
import json

@api.route('/registe', methods=['POST'])
def registe():
    fetched = request.get_json()
    user = User.query.filter_by(email=fetched['email']).first()
    if not user:
        try:
            user_schema = UserSchema()
            user, error = user_schema.load(fetched)
            user = user_schema.dump(user.create()).data
            return response_with(resp.SUCCESS_200)

        except Exception as e:
            return response_with(resp.SERVER_ERROR_500)
    else:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/login', methods=['POST'])
def login():
    fetched = request.get_json()
    try:
        user = User.query.filter_by(email = fetched['email']).first()
        if user and user.password_is_valid(fetched['password']):
            access_token = {
                'token': str(user.generate_token(user.id))
            }
            if access_token:
                return response_with(resp.SUCCESS_200, value={
                    'data': access_token
                })
        else:
            return response_with(resp.INVALID_INPUT_422)
    except Exception as e:
        return response_with(resp.INVALID_INPUT_422)
