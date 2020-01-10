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

WORKDIR /home/admin

COPY . .

# add user admin
RUN useradd -ms /bin/bash admin && \
    echo "admin        ALL=(ALL)       NOPASSWD:ALL" >> /etc/sudoers

USER admin

CMD export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && \
    sudo service postgresql start && \
    flask run -h 0.0.0.0
