from flask import request
from . import api
from api.models.info import Info, InfoSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/infos', methods=['GET'])
def get_infos():
    resource = Info.query.all()
    info_schema = InfoSchema(many=True)
    data = info_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/infos', methods=['POST'])
def add_info():
    try:
        fetched = request.get_json()
        info_schema = InfoSchema()
        info, error = info_schema.load(fetched)
        data = info_schema.dump(info.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/infos/<int:id>', methods=['PUT'])
def update_info(id):
    fetched = request.get_json()
    resource = Info.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    info_schema = InfoSchema()
    data = info_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/infos/<int:id>', methods=['DELETE'])
def delete_info(id):
    resource = Info.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)

@api.route('/infos/<int:id>/categories', methods=['GET'])
def get_info_categories(id):
    info = Info.query.get_or_404(id)
    info_schema = InfoSchema(many=True)
    fetched = info_schema.dump(info).data
    data = fetched['categories']
    return response_with(resp.SUCCESS_200, value={
        'categories': data
    })
