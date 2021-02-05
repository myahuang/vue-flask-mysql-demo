# vue-flask-mysql-demo
backend admin template

# 前端
## vue-admin-beautiful
项目地址：https://github.com/chuzhixin/vue-admin-beautiful.git
https://cloud.tencent.com/developer/article/1475484
滑动刷新token授权
https://www.cnblogs.com/laozhang-is-phi/p/10462316.html
https://segmentfault.com/a/1190000020210980
# 后端
## flask-restful-example
https://github.com/lalala223/flask-restful-example.git
## jwt 用户认证授权
https://blog.csdn.net/yilovexing/article/details/104010890
https://github.com/zhouwei713/flask-webauth
https://juejin.im/post/5d2fec236fb9a07ef161b9e4
sphinx api文档生成
https://www.jianshu.com/p/d4a1347f467b

#部署
* 前端 vue pm2 nginx docker
https://segmentfault.com/a/1190000021395244
vue-cli部署
https://cli.vuejs.org/guide/deployment.html#github-pages
* 后端 flask mysql gunicorn nginx docker
* 前后端服务编排 docker compose

#install
*首次运行打开backend/startup.sh 中的注释部分

注册管理员信息
curl -d '{"email":"admin@qq.com", "username": "admin", "permission": "superAdmin", "password": "admin123" }' -H "Content-Type: application/json" -X POST http://localhost:5000/api/v1/register

登录测试
curl -d '{"username": "admin", "password": "admin123" }' -H "Content-Type: application/json" -X POST http://localhost:5000/api/v1/login

# 注意配置文件端口号问题nginx
前端nginx代理静态页面，转发到nginx容器，nginx代理前后端页面接口

create table users(
      id int identity(1,1),
      username varchar(100),
      email varchar(100),
      login_time varchar(100),
)
