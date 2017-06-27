from flask import request
from . import api
from api.models.library import Library, LibrarySchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/libraries', methods=['GET'])
def get_libraries():
    resource = Library.query.all()
    library_schema = LibrarySchema(many=True)
    data = library_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/libraries', methods=['POST'])
def add_library():
    try:
        fetched = request.get_json()
        library_schema = LibrarySchema()
        library, error = library_schema.load(fetched)
        data = library_schema.dump(library.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/libraries/<int:id>', methods=['PUT'])
def update_library(id):
    fetched = request.get_json()
    resource = Library.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    library_schema = LibrarySchema()
    data = library_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/libraries/<int:id>', methods=['DELETE'])
def delete_library(id):
    resource = Library.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
