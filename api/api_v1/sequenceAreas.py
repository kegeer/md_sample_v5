from flask import request
from . import api
from api.models.sequenceArea import SequenceArea, SequenceAreaSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/sequence_areas', methods=['GET'])
def get_sequence_areas():
    resource = SequenceArea.query.all()
    sequence_area_schema = SequenceAreaSchema(many=True)
    data = sequence_area_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/sequence_areas', methods=['POST'])
def add_sequence_area():
    try:
        fetched = request.get_json()
        sequence_area_schema = SequenceAreaSchema()
        sequence_area, error = sequence_area_schema.load(fetched)
        data = sequence_area_schema.dump(sequence_area.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/sequence_areas/<int:id>', methods=['PUT'])
def update_sequence_area(id):
    fetched = request.get_json()
    resource = SequenceArea.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    sequence_area_schema = SequenceAreaSchema()
    data = sequence_area_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/sequence_areas/<int:id>', methods=['DELETE'])
def delete_sequence_area(id):
    resource = SequenceArea.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
