#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

from . import db
from .base import BaseModel


class ProfilesModel(db.Model, BaseModel):
    """
    示例模型类
    """
    __tablename__ = 'profiles'
    nickname = db.Column(db.String(32))
    signature = db.Column(db.String(32))

