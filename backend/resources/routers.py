#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/19 3:25 下午
# software: PyCharm
from flask_restful import Resource, inputs
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
from common.decorators import login_required
import json, os


class routerResource(Resource):
    """
    router list资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    @login_required
    def get(self):
        """
        获取路由信息
        :return: json
        """
        filePath = os.path.join(os.path.join(os.getcwd(), 'router.json'))
        with open(filePath, 'r') as load_f:
            print(load_f)
            load_dict = json.load(load_f)
        return pretty_result(code.OK, data=load_dict["data"])
