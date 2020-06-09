#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/9 9:50 上午
# software: PyCharm

# parser.add_argument('birthday', type=inputs, help='生日字段验证')
# # 验证日期
# parser.add_argument('birthday',type=inputs.date,help='生日字段验证')
# # 利用正则表达式验证手机号码
# parser.add_argument('telphone',type=inputs.regex(r'1[3578]\d{9}'))
# # 验证输入的url地址
# parser.add_argument('home_page',type=inputs.url,help='个人中心链接验证错误')
# parser.add_argument('username',type=str,help='用户名验证错误',default="angle")
# parser.add_argument('password',type=str,help=u'密码验证错误',required=True,trim=True)
# parser.add_argument('password',type=int,help=u'年龄验证错误')
# parser.add_argument('gender',type=str,choices=['male','female','secret'],help="性别验证错误")


def password_len(value, name):
    if not value:
        raise ValueError(name + ' is required')
    elif len(value) < 8:
        raise ValueError(name + '密码必须8位以上')
    return value
