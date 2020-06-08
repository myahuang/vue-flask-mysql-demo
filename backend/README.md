# Flask-RESTful Example 

## 框架设计
* 启动 gunicorn
* 配置
* 日志（logging）
* 数据初始化迁移 flask-migrate
* 数据库操作 sqlalchemy
* Restful设计风格
* 路由（蓝图）
* 参数验证（RequestParser）
* 单元测试 unittest
* token（pyjwt）
* 部署（docker）

#### 安装依赖包
```
python install -r requirements.txt
```

### 创建数据库
```
$ mysql -uroot -p xxxxxxx
$ create database demo default charset utf8;
```

#### 创建数据表
```
python manager.py db init
python manager.py db migrate -m "版本名后缀"
python manager.py db upgrade
```

#### debug模式启动
```
python manager.py debug
```

#### 生产模式启动
```
python manager.py run
```

#### Tests
```
python -m tests.testapp
```