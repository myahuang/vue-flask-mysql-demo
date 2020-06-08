#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/8 10:14 下午
# software: PyCharm

from flask import jsonify, request
from models.users import UsersModel
from .auths import Auth
from models import db
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
import logging

logger = logging.getLogger(__name__)


class UserResource(Resource):
    """
    示例profile list资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    def get(self):
        self.parser.add_argument("page_num", type=int, required=True, location="json", default=1, help='Rate cannot be converted')
        args = self.parser.parse_args()
        print(args)
        item = {'a': 'b'}
        return pretty_result(code.OK, data=item)

    def post(self):
        self.parser.add_argument("page_num", type=int, required=True, location="json", default=1, help='Rate cannot be converted')
        args = self.parser.parse_args()
        print(args)
        logger.error('test')
        item = {'a': 'bc'}
        return pretty_result(code.OK, data=item)

# def init_api(app):
#     @app.route('/register', methods=['POST'])
#     def register():
#         """
#         用户注册
#         :return: json
#         """
#         email = request.form.get('email')
#         username = request.form.get('username')
#         password = request.form.get('password')
#         user = Users(email=email, username=username, password=Users.set_password(Users, password))
#         result = Users.add(Users, user)
#         if user.id:
#             returnUser = {
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email,
#                 'login_time': user.login_time
#             }
#             return jsonify(common.trueReturn(returnUser, "用户注册成功"))
#         else:
#             return jsonify(common.falseReturn('', '用户注册失败'))
#
#
#     @app.route('/login', methods=['POST'])
#     def login():
#         """
#         用户登录
#         :return: json
#         """
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if (not username or not password):
#             return jsonify(common.falseReturn('', '用户名和密码不能为空'))
#         else:
#             return Auth.authenticate(Auth, username, password)
#
#
#     @app.route('/user', methods=['GET'])
#     def get():
#         """
#         获取用户信息
#         :return: json
#         """
#         result = Auth.identify(Auth, request)
#         if (result['status'] and result['data']):
#             user = Users.get(Users, result['data'])
#             returnUser = {
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email,
#                 'login_time': user.login_time
#             }
#             result = common.trueReturn(returnUser, "请求成功")
#         return jsonify(result)