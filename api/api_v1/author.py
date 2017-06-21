from flask import flash, request
from api.models.model_author import Author, AuthorSchema
from . import api
from api.utils.response import response_with
from api.utils import response as resp
import json

@api.route('/authors', methods=['POST'])
def create_author():
    # data = request.get_json()
    # author_schema = AuthorSchema()
    # author, error = author_schema.load(data)
    # try:
    #     data = request.get_json()
    #     author_schema = AuthorSchema()
    #     author, error = author_schema.load(data)
    #     result = author_schema.dump(author.create()).data
    #     return response_with(resp.SUCCESS_200, value={"author": result})
    # except Exception:
    #     return response_with(resp.INVALID_INPUT_422)
    data = request.get_json()
    author_schema = AuthorSchema()
    author, error = author_schema.load(data)
    return json.dumps(data)
    result = author_schema.dump(author.create()).data
    return response_with(resp.SUCCESS_200, value={"author": result})

@api.route('/authors', methods=['GET'])
def get_authors():
    fetched = Author.query.all()
    author_schema = AuthorSchema(many=True, only=['name', 'surname'])
    authors, error = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"authors": authors})


@api.route('/authors/<int:author_id>', methods=['GET'])
def get_author_detail(author_id):
    fetched = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    author, error = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={'author': author})
