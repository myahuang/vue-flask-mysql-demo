#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

OK = 0

DB_ERROR = 4001

PARAM_ERROR = 4101

AUTHORIZATION_ERROR = 403  # 4201

UNKNOWN_ERROR = 4301

REQUEST_SUCCESS = 200

CREATE_SUCCESS = 201

REQUEST_ERROR = 400

UNAUTHORIZATION_ERROR = 401

NO_ACCESS_ERROR = 403

INVALID_URL_ERROR = 404

SERVER_ERROR = 500

ERROR = -1

CODE_MSG_MAP = {
    OK: 'ok',
    DB_ERROR: '数据库错误',
    PARAM_ERROR: '请求参数错误',
    AUTHORIZATION_ERROR: '认证授权错误',
    UNKNOWN_ERROR: "未知错误",
    REQUEST_SUCCESS: "请求成功",
    CREATE_SUCCESS: "创建成功",
    REQUEST_ERROR: "错误的请求",
    UNAUTHORIZATION_ERROR: "未授权",
    NO_ACCESS_ERROR: "无权限访问",
    INVALID_URL_ERROR: "无效的请求地址",
    SERVER_ERROR: "服务器内部错误",
    ERROR: "业务错误，具体原因看 msg"
}
