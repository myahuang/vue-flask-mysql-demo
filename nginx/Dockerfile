FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
ADD frontend/conf/frontend.conf /etc/nginx/conf.d/
ADD backend/conf/backend.conf /etc/nginx/conf.d/