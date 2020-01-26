FROM ubuntu:latest

# install sudo
RUN apt-get update && \
    apt-get install sudo

# install postgres client
RUN apt-get update && \
    apt-get install postgresql-client -y

#install pip3
RUN apt-get update && \
    apt install python3-pip -y && \
    pip3 install -U Flask

RUN pip3 install requests

#for developing
RUN apt-get install vim -y

# add user admin without privileges
RUN useradd -ms /bin/bash admin

WORKDIR /home/admin

# install postgres driver to use it in flask
RUN apt-get update && \
    pip3 install virtualenv && \
    virtualenv --python=/usr/bin/python3 venvs/postgres && \
    apt-get install libpq-dev python-dev -y && \
    /home/admin/venvs/postgres/bin/pip install psycopg2 && \
    pip3 install psycopg2 && \
    pip3 install flask-jwt-extended && \
    pip3 install flask-hashing && \
    pip3 install flask-sqlalchemy

COPY . .

RUN chown -R admin:admin ./

USER admin
