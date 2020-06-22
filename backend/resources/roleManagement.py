#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/21 9:46 下午
# software: PyCharm

from flask import jsonify, request, current_app, g
from models.users import UsersModel
from models import db
from flask_restful import Resource, inputs
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
from common.vaild import password_len
from sqlalchemy.exc import SQLAlchemyError
from common.decorators import login_required


class RoleManagementResource(Resource):
    """
    users list资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    @login_required
    def get(self):
        """
        获取用户列表信息
        :return: json
        """
        user = UsersModel.get(UsersModel, g.user_id)
        returnUser = {
            'id': user.id,
            'userName': user.username,
            'email': user.email,
            'permission': user.permission,
            'avatar': user.avatar
            # 'login_time': user.login_time
        }
        totalCount = 3;
        List = [{
            "id": "@id",
            "permission": "editor",
          }]
        return pretty_result(code.OK, data=List)

    @login_required
    def post(self):
        user = UsersModel.get(UsersModel, g.user_id)
        returnUser = {
            'id': user.id,
            'userName': user.username,
            'email': user.email,
            'permission': user.permission,
            'avatar': user.avatar
            # 'login_time': user.login_time
        }
        return pretty_result(code.OK, data=returnUser)

