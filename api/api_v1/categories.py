from flask import request
from . import api
from api.models.category import Category, CategorySchema
from api.utils.response import response_with
import api.utils.response as resp

@api.route('/categories', methods=['GET'])
def get_categories():
    resource = Category.query.all()
    category_schema = CategorySchema(many=True)
    data = category_schema.dump(resource).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/categories', methods=['POST'])
def add_category():
    try:
        fetched = request.get_json()
        category_schema = CategorySchema()
        category, error = category_schema.load(fetched)
        data = category_schema.dump(category.create()).data
        return response_with(resp.SUCCESS_200, value={
            'data': data
        })
    except:
        return response_with(resp.INVALID_INPUT_422)

@api.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    fetched = request.get_json()
    resource = Category.query.get_or_404(id)
    for key, value in fetched.items():
        setattr(resource, key, value)
    category_schema = CategorySchema()
    data = category_schema.dump(resource.update()).data
    return response_with(resp.SUCCESS_200, value={
        'data': data
    })

@api.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    resource = Category.query.get_or_404(id)
    resource.delete()
    return response_with(resp.SUCCESS_200)
