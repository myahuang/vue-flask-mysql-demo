#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/8 10:14 下午
# software: PyCharm

from flask import jsonify, request, current_app
from models.users import UsersModel
from models import db
from flask_restful import Resource, inputs
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
from common.vaild import password_len
from sqlalchemy.exc import SQLAlchemyError
from common.decorators import login_required


class UserResource(Resource):
    """
    示例profile list资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    @login_required
    def get(self):
        """
        获取用户信息
        :return: json
        """
        # result = Auth.identify(Auth, request)
        # print(result)
        # if (result['code']==0 and result['data']):
        # user = UsersModel.get(UsersModel, result['data'])
        # returnUser = {
        #     'id': user.id,
        #     'username': user.username,
        #     'email': user.email,
        #     'login_time': user.login_time
        # }
        returnUser = ''
        result = pretty_result(code.OK, data=returnUser, msg='请求成功')
        return result

    def post(self):
        self.parser.add_argument("page_num", type=int, required=True, location="json", default=1, help='Rate cannot be converted')
        args = self.parser.parse_args()
        print(args)
        item = {'a': 'bc'}
        return pretty_result(code.OK, data=item)

