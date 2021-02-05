#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/9 10:41 上午
# software: PyCharm

from flask import jsonify, request, current_app, g
from models.users import UsersModel
from .auths import AuthorizationResource
from models import db
from flask_restful import Resource, inputs
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
from common.vaild import password_len
from common.decorators import login_required


class RegisterResource(Resource):
    """
    用户注册
    """

    def __init__(self):
        self.parser = RequestParser()

    def post(self):
        """
        用户注册
        :return: json
        """
        self.parser.add_argument("email", type=inputs.regex(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'), required=True, location="json",
                                 help='email format is incorrect')
        self.parser.add_argument("username", type=str, required=True, location="json",
                                 help='username is required')
        self.parser.add_argument("permission", type=str, choices=['test', 'guest', 'user', 'admin', 'superAdmin'], required=True, location="json",
                                 help='permission is required and only (test,user,admin,superAdmin)')
        self.parser.add_argument("password", type=password_len, required=True, location="json", trim=True)
        args = self.parser.parse_args()
        user = UsersModel(email=args.email, username=args.username, password=UsersModel.set_password(UsersModel, args.password), permission=args.permission)
        result = UsersModel.add(UsersModel, user)
        if user.id:
            returnUser = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'login_time': user.login_time
            }
            return pretty_result(code.OK, data=returnUser, msg='用户注册成功')
        else:
            return pretty_result(code.ERROR, data='', msg='用户注册失败(用户名或邮箱已存在)')


class LoginResource(Resource):
    """
    用户登陆
    """

    def __init__(self):
        self.parser = RequestParser()

    def post(self):
        """
        用户登陆
        :return: json
        """
        self.parser.add_argument("username", type=str, required=True, location="json",
                                 help='userName is required')
        self.parser.add_argument("password", type=password_len, required=True, location="json", trim=True)
        args = self.parser.parse_args()
        return AuthorizationResource.post(AuthorizationResource, args.username, args.password)


class LogoutResource(Resource):
    """
    用户退出
    """

    def __init__(self):
        self.parser = RequestParser()

    @login_required
    def post(self):
        '''
        存在的两个问题
        用户登出
        前端可以直接丢弃当前的 access token，当然，如果再严谨些，后端最好有一个 redis 之类的缓存数据库，如果用户登出，则把对应的 token 加入到缓存中，如果再有请求携带该 token 时，则要先到缓存中查看 token 是否存在，如果存在，那么就要返回该 token 已经是非法的 token 了。
        token 过期续期
        这个问题就可以用到 refresh token 了，当前端根据 access token expire 发现用户的 access token 快要过期时，则使用 refresh token 到后端获取新的 access token，只要保证 refresh token 的过期时间长于 access token 的就可以了。
        '''
        return pretty_result(code.OK, msg='退出成功！')

