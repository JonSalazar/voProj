#!/bin/bash

# running postgres
if [ $1 = "start_docker" ]; then
    mkdir -p $HOME/docker/volumes/postgres
    docker pull postgres:12.1
    docker run --rm --name psql-container -e POSTGRES_PASSWORD=pass123 -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data -d postgres:12.1
fi

# running app
docker build -t vivaorganica_1 -f Dockerfile .
docker run --rm --name app-container -p 5000:5000 --link psql-container -it vivaorganica_1
