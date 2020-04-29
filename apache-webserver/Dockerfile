FROM ubuntu:latest
RUN apt-get update && apt install -y apache2 apache2-doc apache2-utils 
ENTRYPOINT ["apache2ctl"]
CMD ["-D","FOREGROUND"]
EXPOSE 80


