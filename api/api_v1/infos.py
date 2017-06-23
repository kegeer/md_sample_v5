# from flask import request
# from api.utils.database import db
# from api.models.info import Info, InfoSchema
# from . import api
# from api.utils.response import response_with
# import api.utils.response as resp
#
# @api.route('/infos', methods=['GET'])
# def get_infos():
#     fetched = Info.query.all()
#     info_schema = InfoSchema()
#     data = info_schema.dump(fetched).data
#     return response_with(resp.SUCCESS_200, value={
#         'infos': data
#     })
#
# @api.route('/infos', methods=['POST'])
# def create_info():
#     fetched = request.get_json()
#     info_schema = InfoSchema()
#     info, error = info_schema.load(fetched)
#     data = info_schema.dump(info).data
#     return response_with(resp.SUCCESS_200, value={
#         'info': data
#     })
#
# @api.route('/infos/<int:id>', methods=['GET'])
# def get_info_detail(id):
#     info = Info.query.get_or_404(id)
#     info_schema = InfoSchema()
#     data = info_schema.dump(info).data
#     return response_with(resp.SUCCESS_200, value={
#         'info': data
#     })
#
# @api.route('/infos/<int:id>', methods=['PUT'])
# def update_info(id):
#     fetched = request.json()
#     info_schema = InfoSchema()
#     info, error = info_schema.load(info_data)
#     data = info_schema.dump(info.update()).data
#     return response_with(resp.SUCCESS_200, value={
#         'info': data
#     })
#
# @api.route('/infos/<int:id>', methods=['DELETE'])
# def delete_info(id):
#     info = Info.query.get_or_404(id)
#     info_schema = InfoSchame()
#     data = info_schema.dump(info.delete()).data
#     return response_with(resp.SUCCESS_200)
#
# # @api.route('/infos/<int:id>/categories', methods=['GET'])
# # def get_info_categories(id):
# #     info = Info.query.get_or_404(id)
# #     info_schema = InfoSchema()
# #     fetched = info_schema.dump(info).data
# #     data = fetched['categories']
# #     return response_with(resp.SUCCESS_200, value={
# #         'categories': data
# #     })
