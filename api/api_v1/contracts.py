from flask import request
from . import api
from api.models.contract import Contract, ContractSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/contracts', methods=['GET'])
def get_contracts():
    resource = Contract.query.all()
    contract_schema = ContractSchema(many=True)
    data = contract_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/contracts', methods=['POST'])
def add_contract():
    try:
        fetched = request.get_json()
        contract_schema = ContractSchema()
        contract, error = contract_schema.load(fetched)
        data = contract_schema.dump(contract.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/contracts/<int:id>', methods=['PUT'])
def update_contract(id):
    fetched = request.get_json()
    resource = Contract.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    contract_schema = ContractSchema()
    data = contract_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/contracts/<int:id>', methods=['DELETE'])
def delete_contract(id):
    resource = Contract.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
