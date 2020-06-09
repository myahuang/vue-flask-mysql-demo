#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/9 2:38 下午
# software: PyCharm

from flask import request, g
from .jwt_util import verify_jwt


def jwt_authentication():
    """
    根据jwt验证用户身份
    """
    g.user_id = None
    g.is_refresh_token = False
    authorization = request.headers.get('Authorization')
    if authorization and authorization.startswith('Bearer '): # 让前端请求头携带Authorization，值以'Bearer '开头
        token = authorization.strip()[7:]
        payload = verify_jwt(token)
        if payload:
            g.user_id = payload.get('user_id')
            g.is_refresh_token = payload.get('refresh')
