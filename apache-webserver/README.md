

#BUILD image
docker build -t apachewebserver .

#RUN container
docker run -it -p 80:80 -v /<path-of-file>/:/var/www/html/ apachewebserver