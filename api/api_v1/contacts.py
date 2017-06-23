from flask import request
from . import api
from api.models.contact import Contact, ContactSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/agencies/<int:agency_id>/contacts', methods=['GET'])
def get_agency_contacts(agency_id):
    resource = Contact.query.filter_by(agency_id=agency_id)
    contact_schema = ContactSchema()
    data = contact_schema.dump(resource, many=True).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/contacts', methods=['GET'])
def get_contacts():
    resource = Contact.query.all()
    contact_schema = ContactSchema()
    data = contact_schema.dump(resource, many=True).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/contacts', methods=['POST'])
def add_contact():
    fetched = request.get_json()
    contact_schema = ContactSchema()
    contact, error = contact_schema.load(fetched)
    data = contact_schema.dump(contact.create()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    fetched = request.get_json()
    resource = Contact.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    contact_schema = ContactSchema()
    data = contact_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    resource = Contact.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
