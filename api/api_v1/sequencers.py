from flask import request
from . import api
from api.models.sequencer import Sequencer, SequencerSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/sequencers', methods=['GET'])
def get_sequencers():
    resource = Sequencer.query.all()
    sequencer_schema = SequencerSchema(many=True)
    data = sequencer_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/sequencers', methods=['POST'])
def add_sequencer():
    try:
        fetched = request.get_json()
        sequencer_schema = SequencerSchema()
        sequencer, error = sequencer_schema.load(fetched)
        data = sequencer_schema.dump(sequencer.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/sequencers/<int:id>', methods=['PUT'])
def update_sequencer(id):
    fetched = request.get_json()
    resource = Sequencer.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    sequencer_schema = SequencerSchema()
    data = sequencer_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/sequencers/<int:id>', methods=['DELETE'])
def delete_sequencer(id):
    resource = Sequencer.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
