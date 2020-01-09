FROM ubuntu:latest

# install sudo
RUN apt-get update && \
    apt-get install sudo

# add postgres user
RUN useradd -ms /bin/bash postgres && \
    echo "postgres        ALL=(ALL)       NOPASSWD:ALL" >> /etc/sudoers

# install postgres
RUN su postgres && \
    sudo apt-get update -y && \
    sudo apt-get install postgresql postgresql-contrib -y && \
    sudo service postgresql start

#install pip3
RUN sudo apt-get update && \
    sudo apt install python3-pip -y && \
    pip3 install -U Flask

#for developing
RUN sudo apt-get install vim -y

WORKDIR /home/postgres

COPY . .

ENTRYPOINT export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && \
    flask run -h 0.0.0.0 && \
    su admin && \
    service postgresql start && \
    python3 app.py
