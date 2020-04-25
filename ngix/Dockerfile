FROM ubuntu:latest

MAINTAINER abhinavkishoregv

RUN apt-get update && apt-get upgrade -y
RUN apt-get install nginx -y
ADD index.html /usr/share/nginx/html/index.html

ENTRYPOINT ["/usr/sbin/nginx","-g","daemon off;"]

EXPOSE 80