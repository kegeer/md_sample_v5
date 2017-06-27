from flask import request
from . import api
from api.models.subproject import Subproject, SubprojectSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/subprojects', methods=['GET'])
def get_subprojects():
    resource = Subproject.query.all()
    subproject_schema = SubprojectSchema(many=True)
    data = subproject_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/subprojects', methods=['POST'])
def add_subproject():
    try:
        fetched = request.get_json()
        subproject_schema = SubprojectSchema()
        subproject, error = subproject_schema.load(fetched)
        data = subproject_schema.dump(subproject.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/subprojects/<int:id>', methods=['PUT'])
def update_subproject(id):
    fetched = request.get_json()
    resource = Subproject.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    subproject_schema = SubprojectSchema()
    data = subproject_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/subprojects/<int:id>', methods=['DELETE'])
def delete_subproject(id):
    resource = Subproject.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)

@api.route('/projects/<int:project_id>/subprojects', methods=['GET'])
def get_project_subprojects(project_id):
    resource = Subproject.query.filter_by(project_id=project_id)
    subproject_schame = SubprojectSchema(many=True, exclude=('pmid', 'ori_num', 'type', 'amount'))
    data = subproject_schame.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })
