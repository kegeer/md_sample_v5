from flask import request
from . import api
from api.models.ref import Ref, RefSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/refs', methods=['GET'])
def get_refs():
    resource = Ref.query.all()
    ref_schema = RefSchema(many=True)
    data = ref_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/refs', methods=['POST'])
def add_ref():
    try:
        fetched = request.get_json()
        ref_schema = RefSchema()
        ref, error = ref_schema.load(fetched)
        data = ref_schema.dump(ref.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/refs/<int:id>', methods=['PUT'])
def update_ref(id):
    fetched = request.get_json()
    resource = Ref.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    ref_schema = RefSchema()
    data = ref_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/refs/<int:id>', methods=['DELETE'])
def delete_ref(id):
    resource = Ref.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
