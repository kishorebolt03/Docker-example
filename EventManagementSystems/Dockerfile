FROM php:7.3-apache
#Install git
RUN apt-get update &&  apt-get install  git -y 
RUN docker-php-ext-install pdo pdo_mysql mysqli

EXPOSE 80
EXPOSE 3306