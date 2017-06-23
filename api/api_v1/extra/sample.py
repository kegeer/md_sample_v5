from flask import request
from flask_restful import Resource
from api.models.sample import Sample, SampleSchema
from api.utils.response import response_with
import api.utils.response as resp

sample_schema = SampleSchema()

class Sample(Resource):
    def get(self, client_id=None):
        if sample_id not None:
            sample = Sample.query.get_or_404(sample_id)
            if sample not None:
                data = sample_schema.dump(sample).data
                return response_with(resp.SUCCESS_200, value={
                    'sample': data
                })
        samples = Sample.query.all()
        data = sample_schema.dump(samples, many=True).data
        return response_with(resp.SUCCESS_200, value={
            'samples': data
        })
    def post(self):
        fetched = request.get_json()
        if len(fetched) > 0:
            sample, error = sample_schema.load(fetched)
            data = sample_schema.dump(sample.add()).data
            return response_with(resp.SUCCESS_200, value={
                'sample': data
            })
    def update(self, sample_id):
        fetched = request.get_json()
        sample = Sample.query.get_or_404(sample_id)
        if sample not None:
            for key, value in fetched.items():
                setattr(sample, key, value)
            data = sample_schema.dump(sample.update()).data
            response_with(resp.SUCCESS_200, value={
                'sample': data
            })

    def delete(self, sample_id):
        sample = Sample.query.get_or_404(sample_id)
        if sample not None:
            sample.delete()
            return response_with(resp.SUCCESS_200)
