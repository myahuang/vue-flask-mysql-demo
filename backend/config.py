#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

import os
import multiprocessing
basedir = os.path.abspath(os.path.dirname(__file__))

MODE = 'develop'  # develop: 开发模式; production: 生产模式


class ProductionConfig(object):
    """
    生产配置
    """
    BIND = '0.0.0.0:5000'
    WORKERS = multiprocessing.cpu_count() * 2 + 1
    WORKER_CONNECTIONS = 10000
    BACKLOG = 64
    TIMEOUT = 60
    LOG_LEVEL = 'INFO'
    LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), 'logs')
    LOG_FILE_MAX_BYTES = 1024 * 1024 * 100
    LOG_FILE_BACKUP_COUNT = 10
    PID_FILE = 'run.pid'
    # sqlite 数据库配置
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'example.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOSTNAME = 'container_mysql'
    PORT = '3306'
    DATABASE = 'demo'
    USERNAME = 'root'
    PASSWORD = 'password'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/tushare?charset=utf8'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT,
                                                                                   DATABASE)
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BASEDIR = basedir
    # 安全配置
    CSRF_ENABLED = True
    SECRET_KEY = 'jklklsadhfjkhwbii9/sdf\sdf'
    JWT_EXPIRY_HOURS = 1
    JWT_REFRESH_DAYS = 1
    JWT_SECRET = 'jklklsadhfjkhwbii9/sdf\sdf'


class DevelopConfig(object):
    """
    开发配置
    """
    BIND = '0.0.0.0:5000'
    WORKERS = 2
    WORKER_CONNECTIONS = 1000
    BACKLOG = 64
    TIMEOUT = 30
    LOG_LEVEL = 'DEBUG'
    LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), 'logs')
    LOG_FILE_MAX_BYTES = 1024 * 1024
    LOG_FILE_BACKUP_COUNT = 1
    PID_FILE = 'run.pid'
    # sqlite 数据库配置
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'example.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@127.0.0.1/demo"
    HOSTNAME = 'container_mysql'
    PORT = '3306'
    DATABASE = 'demo'
    USERNAME = 'root'
    PASSWORD = 'password'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/tushare?charset=utf8'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT,
                                                                                   DATABASE)

    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BASEDIR = basedir
    # 安全配置
    CSRF_ENABLED = True
    SECRET_KEY = 'jklklsadhfjkhwbii9/sdf\sdf'
    JWT_EXPIRY_HOURS = 1
    JWT_REFRESH_DAYS = 1
    JWT_SECRET = 'jklklsadhfjkhwbii9/sdf\sdf'


if MODE == 'production':
    config = ProductionConfig
else:
    config = DevelopConfig

