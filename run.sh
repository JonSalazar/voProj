#!/bin/bash

docker build -t vivaorganica_1 -f Dockerfile .

if [ $1 == bash ]; then
    docker run -p 5000:5000 --rm -it vivaorganica_1 /bin/bash
else
    docker run -p 5000:5000 --rm -it vivaorganica_1
fi
