from flask import request
from . import api
from api.models.project import Project, ProjectSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/projects', methods=['GET'])
def get_projects():
    resource = Project.query.all()
    project_schema = ProjectSchema(many=True)
    data = project_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/projects', methods=['POST'])
def add_project():
    try:
        fetched = request.get_json()
        project_schema = ProjectSchema()
        project, error = project_schema.load(fetched)
        data = project_schema.dump(project.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/projects/<int:id>', methods=['PUT'])
def update_project(id):
    fetched = request.get_json()
    resource = Project.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    project_schema = ProjectSchema()
    data = project_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    resource = Project.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
