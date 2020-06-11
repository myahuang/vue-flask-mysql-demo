#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/9 2:48 下午
# software: PyCharm
from functools import wraps
from flask import g
from common import code, pretty_result


def login_required(func):
    """
    用户必须登录装饰器
    使用方法：放在method_decorators中
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not g.user_id:
            return pretty_result(code.UNAUTHORIZATION_ERROR, msg='User must be authorized.')
            # return {'message': 'User must be authorized.'}, 401
        elif g.is_refresh_token:
            return pretty_result(code.AUTHORIZATION_ERROR, msg='Do not use refresh token.')
            # return {'message': 'Do not use refresh token.'}, 403
        else:
            return func(*args, **kwargs)

    return wrapper
