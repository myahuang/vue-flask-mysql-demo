#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

from flask import Blueprint
from flask_restful import Api
from resources import profiles
from resources import users

api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)

api.add_resource(profiles.ProfileListResource, '/profiles', endpoint = 'tasks')
api.add_resource(profiles.ProfileResource, '/profiles/<string:id>')
api.add_resource(users.UserResource, '/test')