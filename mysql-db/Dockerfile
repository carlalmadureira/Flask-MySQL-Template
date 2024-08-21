FROM mysql:latest 
ENV MYSQL_DATABASE appdb

VOLUME . /var/lib/mysql
COPY . /docker-entrypoint-initdb.d/
