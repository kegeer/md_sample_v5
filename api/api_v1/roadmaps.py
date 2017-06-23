from flask import request
from . import api
from api.models.roadmap import Roadmap, RoadmapSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/roadmaps', methods=['GET'])
def get_roadmaps():
    resource = Roadmap.query.all()
    roadmap_schema = RoadmapSchema(many=True)
    data = roadmap_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/roadmaps', methods=['POST'])
def add_roadmap():
    try:
        fetched = request.get_json()
        roadmap_schema = RoadmapSchema()
        roadmap, error = roadmap_schema.load(fetched)
        data = roadmap_schema.dump(roadmap.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/roadmaps/<int:id>', methods=['PUT'])
def update_roadmap(id):
    fetched = request.get_json()
    resource = Roadmap.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    roadmap_schema = RoadmapSchema()
    data = roadmap_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/roadmaps/<int:id>', methods=['DELETE'])
def delete_roadmap(id):
    resource = Roadmap.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
