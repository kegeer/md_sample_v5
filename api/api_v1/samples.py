from flask import request
from . import api
from api.models.sample import Sample, SampleSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/batches/<int:batch_id>/samples', methods=['GET'])
def get_agency_samples(batch_id):
    resource = Sample.query.filter_by(batch_id=batch_id)
    sample_schema = SampleSchema(many=True, exclude=('pmid', 'ori_num', 'type', 'amount'))
    data = sample_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/samples', methods=['GET'])
def get_samples():
    resource = Sample.query.all()
    sample_schema = SampleSchema()
    data = sample_schema.dump(resource, many=True).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/samples', methods=['POST'])
def add_sample():
    fetched = request.get_json()
    # import json
    # return json.dumps(fetched)
    sample_schema = SampleSchema()
    sample, error = sample_schema.load(fetched)
    data = sample_schema.dump(sample.create()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })
    try:
        fetched = request.get_json()
        import json
        return josn.dumps(fetched)
        sample_schema = SampleSchema()
        sample, error = sample_schema.load(fetched)
        data = sample_schema.dump(sample.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/samples/<int:id>', methods=['PUT'])
def update_sample(id):
    fetched = request.get_json()
    resource = Sample.query.get_or_404(id)
    for key, value in fetched:
        setattr(resource, key, value)
    sample_schema = SampleSchema()
    data = sample_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/samples/<int:id>', methods=['DELETE'])
def delete_sample(id):
    resource = Sample.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
