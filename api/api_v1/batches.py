from flask import request
from . import api
from api.models.batch import Batch, BatchSchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/batches', methods=['GET'])
def get_batches():
    resource = Batch.query.all()
    batch_schema = BatchSchema(many=True, exclude=('agency_id', 'contact_id', 'store_time', 'position_id', 'subproject_id', 'roadmap_id', 'remark', 'samples'))
    data = batch_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/batches', methods=['POST'])
def add_batch():
    try:
        fetched = request.get_json()
        batch_schema = BatchSchema()
        batch, error = batch_schema.load(fetched)
        data = batch_schema.dump(batch.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/batches/<int:id>', methods=['PUT'])
def update_batch(id):
    fetched = request.get_json()
    resource = Batch.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    batch_schema = BatchSchema()
    data = batch_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/batches/<int:id>', methods=['DELETE'])
def delete_batch(id):
    resource = Batch.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)

@api.route('/agencies/<int:agency_id>/batches', methods=['GET'])
def get_agency_batches(agency_id):
    resource = Batch.query.filter_by(agency_id=agency_id)
    batch_schema = BatchSchema(many=True)
    data = batch_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })
