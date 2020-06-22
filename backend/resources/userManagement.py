#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/21 9:22 下午
# software: PyCharm

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/8 10:14 下午
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


class UserManagementResource(Resource):
    """
    users management资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    @login_required
    def get(self):
        """
        获取用户列表信息
        :return: json
        """
        self.parser.add_argument("pageNo", type=int, required=True, location="args",
                                 help='pageNo is required')
        self.parser.add_argument("pageSize", type=int, required=True, location="args", help='pageSize is required')
        self.parser.add_argument("username", type=str, required=True, location="args", help='username is required')
        args = self.parser.parse_args()
        user_list = UsersModel.paginate(UsersModel, args.pageNo, args.pageSize)
        items = []
        totalCount = user_list.total;
        user_list = user_list.items
        if args.username:
            user_list = UsersModel.filter_by_username(UsersModel, args.username)
            totalCount = len(user_list)
        for user in user_list:
            items.append(
                {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'permission': user.permission,
                    'avatar': user.avatar,
                    'login_time': user.login_time,
                    'update_time': user.update_time.strftime("%m/%d/%Y %H:%M:%S")
                }
            )
        data = {
            'pageNo': args.pageNo,
            'pageSize': args.pageSize,
            'totalCount': totalCount,
            'items': items
        }
        return pretty_result(code.OK, data=data, msg='用户信息获取成功！')

    @login_required
    def put(self):
        self.parser.add_argument("id", type=int, required=True, location="json", help='id is required')
        self.parser.add_argument("email", type=inputs.regex(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'),
                                 required=True, location="json",
                                 help='email format is incorrect')
        self.parser.add_argument("permission", type=str, choices=['test', 'guest', 'user', 'admin', 'superAdmin'],
                                 required=True, location="json",
                                 help='permission is required and only (test,user,admin,superAdmin)')
        self.parser.add_argument("password", type=password_len, location="json", trim=True)
        args = self.parser.parse_args()
        userEmailInfo = UsersModel.query.filter_by(email=args.email).all()
        for item in userEmailInfo:
            if item.id != args.id:
                return pretty_result(code.ERROR, msg='该邮箱已经被注册！')
        userInfo = UsersModel.query.filter_by(id=args.id).first()
        userInfo.email=args.email
        userInfo.permission=args.permission
        if args.password:
            userInfo.password=UsersModel.set_password(UsersModel, args.password)
        UsersModel.update(userInfo)
        return pretty_result(code.OK, msg='用户信息更新成功！')

    @login_required
    def delete(self):
        self.parser.add_argument("ids", type=list, required=True, location="json", help='ids is required')
        args = self.parser.parse_args()
        UsersModel.delete(UsersModel, args.ids)
        return pretty_result(code.OK, msg='用户信息删除成功！')
