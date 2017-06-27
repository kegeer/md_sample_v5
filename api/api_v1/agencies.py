from flask import request
from . import api
from api.models.agency import Agency, AgencySchema
from api.utils.response import response_with
import api.utils.response as resp
import json

@api.route('/agencies', methods=['GET'])
def get_agencies():
    fetched = Agency.query.all()
    agency_schema = AgencySchema(many=True, exclude=('contacts', 'batches'))
    data = agency_schema.dump(fetched).data
    return response_with(resp.SUCCESS_200, value={"data": data})

@api.route('/agencies', methods=['POST'])
def create_agency():
    try:
        fetched = request.get_json()
        agency_schema = AgencySchema()
        agency, error = agency_schema.load(fetched)
        return str(type(agency))
        data = agency_schema.dump(agency.create()).data
        return response_with(resp.SUCCESS_200, value={
            "data": data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/agencies/<int:id>', methods=['GET'])
def get_agency_detail(id):
    resource = Agency.query.get_or_404(id)
    agency_schema = AgencySchema()
    data = agency_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        "data": data
    })


@api.route('/agencies/<int:id>', methods=['PUT'])
def update_agency(id):
    fetched = request.get_json(force=True)
    resource = Agency.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    agency_schema = AgencySchema()
    data = agency_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        "data": data
    })

@api.route('/agencies/<int:id>', methods=['DELETE'])
def delete_agency(id):
    fetched = Agency.query.get_or_404(id)
    fetched.delete()
    return response_with(resp.SUCCESS_200)
