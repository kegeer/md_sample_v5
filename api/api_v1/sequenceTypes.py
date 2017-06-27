from flask import request
from . import api
from api.models.sequenceType import SequenceType, SequenceTypeSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/sequence_types', methods=['GET'])
def get_sequence_types():
    resource = SequenceType.query.all()
    sequence_type_schema = SequenceTypeSchema(many=True)
    data = sequence_type_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/sequence_types', methods=['POST'])
def add_sequence_type():
    try:
        fetched = request.get_json()
        sequence_type_schema = SequenceTypeSchema()
        sequence_type, error = sequence_type_schema.load(fetched)
        data = sequence_type_schema.dump(sequence_type.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/sequence_types/<int:id>', methods=['PUT'])
def update_sequence_type(id):
    fetched = request.get_json()
    resource = SequenceType.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    sequence_type_schema = SequenceTypeSchema()
    data = sequence_type_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/sequence_types/<int:id>', methods=['DELETE'])
def delete_sequence_type(id):
    resource = SequenceType.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
