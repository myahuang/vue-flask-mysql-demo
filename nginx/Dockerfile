FROM nginx

#RUN rm /etc/nginx/conf.d/default.conf
#RUN rm /etc/nginx/nginx.conf
ADD frontend/conf/frontend.conf /etc/nginx/conf.d/
#ADD backend/conf/backend.conf /etc/nginx/conf.d/

# 拷贝 nginx 全局配置文件
#COPY frontend/conf/frontend.conf /etc/nginx/conf.d/default.conf

# apk 国内源
#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/' /etc/apk/repositories

# 安装 nginx
#RUN apk update \
#    && apk upgrade \
#    && apk add --no-cache openssl \
 #   && apk add --no-cache bash

# 启动 nginx
#CMD nginx -s reload

# 暴露 80 端口和 443 端口给容器外部
EXPOSE 80 443