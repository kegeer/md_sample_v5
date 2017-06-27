from flask import request
from . import api
from api.models.result import Result, ResultSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/results', methods=['GET'])
def get_results():
    resource = Result.query.all()
    result_schema = ResultSchema(many=True)
    data = result_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/results', methods=['POST'])
def add_result():
    try:
        fetched = request.get_json()
        result_schema = ResultSchema()
        result, error = result_schema.load(fetched)
        data = result_schema.dump(result.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/results/<int:id>', methods=['PUT'])
def update_result(id):
    fetched = request.get_json()
    resource = Result.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    result_schema = ResultSchema()
    data = result_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/results/<int:id>', methods=['DELETE'])
def delete_result(id):
    resource = Result.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
