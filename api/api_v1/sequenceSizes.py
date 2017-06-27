from flask import request
from . import api
from api.models.sequenceSize import SequenceSize, SequenceSizeSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/sequence_sizes', methods=['GET'])
def get_sequence_sizes():
    resource = SequenceSize.query.all()
    sequence_size_schema = SequenceSizeSchema(many=True)
    data = sequence_size_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/sequence_sizes', methods=['POST'])
def add_sequence_size():
    try:
        fetched = request.get_json()
        sequence_size_schema = SequenceSizeSchema()
        sequence_size, error = sequence_size_schema.load(fetched)
        data = sequence_size_schema.dump(sequence_size.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/sequence_sizes/<int:id>', methods=['PUT'])
def update_sequence_size(id):
    fetched = request.get_json()
    resource = SequenceSize.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    sequence_size_schema = SequenceSizeSchema()
    data = sequence_size_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/sequence_sizes/<int:id>', methods=['DELETE'])
def delete_sequence_size(id):
    resource = SequenceSize.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
