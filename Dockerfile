FROM ubuntu:latest

# install sudo
RUN apt-get update && \
    apt-get install sudo

# add postgres user
RUN useradd -ms /bin/bash postgres && \
    echo "postgres        ALL=(ALL)       NOPASSWD:ALL" >> /etc/sudoers

# install postgres
USER postgres

RUN sudo apt-get update -y && \
    sudo apt-get install postgresql postgresql-contrib -y

USER root

#install pip3
RUN apt-get update && \
    apt install python3-pip -y && \
    pip3 install -U Flask

RUN pip3 install requests

#for developing
RUN apt-get install vim -y

# add user admin
RUN useradd -ms /bin/bash admin && \
    echo "admin        ALL=(ALL)       NOPASSWD:ALL" >> /etc/sudoers

WORKDIR /home/admin

# install postgres driver to use it in flask
RUN sudo apt-get update && \
    sudo pip3 install virtualenv && \
    virtualenv --python=/usr/bin/python3 venvs/postgres && \
    sudo apt-get install libpq-dev python-dev -y && \
    /home/admin/venvs/postgres/bin/pip install psycopg2 && \
    sudo pip3 install psycopg2

COPY . .

RUN chown -R admin:admin ./

USER admin

CMD export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && \
    sudo service postgresql start && \
    flask run -h 0.0.0.0




