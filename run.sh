#!/bin/bash

docker build -t vivaorganica_1 -f Dockerfile .
docker run -p 5000:5000 --rm -it vivaorganica_1
