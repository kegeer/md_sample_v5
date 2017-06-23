from flask import request
from . import api
from api.models.position import Position, PositionSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/positions', methods=['GET'])
def get_positions():
    resource = Position.query.all()
    position_schema = PositionSchema(many=True)
    data = position_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/positions', methods=['POST'])
def add_position():
    try:
        fetched = request.get_json()
        position_schema = PositionSchema()
        position, error = position_schema.load(fetched)
        data = position_schema.dump(position.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/positions/<int:id>', methods=['PUT'])
def update_position(id):
    fetched = request.get_json()
    resource = Position.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    position_schema = PositionSchema()
    data = position_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/positions/<int:id>', methods=['DELETE'])
def delete_position(id):
    resource = Position.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
