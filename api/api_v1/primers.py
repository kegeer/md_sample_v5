from flask import request
from . import api
from api.models.primer import Primer, PrimerSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/primers', methods=['GET'])
def get_primers():
    resource = Primer.query.all()
    primer_schema = PrimerSchema(many=True)
    data = primer_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/primers', methods=['POST'])
def add_primer():
    try:
        fetched = request.get_json()
        primer_schema = PrimerSchema()
        primer, error = primer_schema.load(fetched)
        data = primer_schema.dump(primer.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/primers/<int:id>', methods=['PUT'])
def update_primer(id):
    fetched = request.get_json()
    resource = Primer.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    primer_schema = PrimerSchema()
    data = primer_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/primers/<int:id>', methods=['DELETE'])
def delete_primer(id):
    resource = Primer.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
