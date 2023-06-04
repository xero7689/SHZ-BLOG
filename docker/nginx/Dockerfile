FROM nginx:latest
LABEL maintainer="volleyp7689@gmail.com"

COPY docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY docker/nginx/blog_nginx.conf /etc/nginx/sites-available/ 

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/\
    && rm /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
