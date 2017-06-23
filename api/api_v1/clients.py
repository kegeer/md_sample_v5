from flask import request
from . import api
from api.models.client import Client, ClientSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/clients', methods=['GET'])
def get_clients():
    resource = Client.query.all()
    client_schema = ClientSchema()
    data = client_schema.dump(resource, many=True).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/clients', methods=['POST'])
def add_client():
    try:
        fetched = request.get_json()
        client_schema = ClientSchema()
        client, error = client_schema.load(fetched)
        data = client_schema.dump(client.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    fetched = request.get_json()
    resource = Client.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    client_schema = ClientSchema()
    data = client_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    resource = Client.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
