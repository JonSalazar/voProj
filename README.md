# Project

## Description

This is an API REST developed with Flask framework and PostgreSQL database.

It uses a DockerFile to create an environment with required dependencies.

## How to run

I need to change the postgres database manually as follow (inside of the container)

```sh
docker build -t vivaorganica_1 -f Dockerfile .
docker run -p 5000:5000 --rm -it vivaorganica_1 /bin/bash
# once you are in the container...
export LC_ALL=C.UTF-8 && export LANG=C.UTF-8
sudo service postgresql start
sudo su postgres
psql -U postgres
# once you are in postgres terminal
\password
# here we use pass123 BUT THIS IS JUST FOR LEARNING, NEVER USE THIS IN A REAL PROJECT

# return to admin user
\q
exit

# migrate database
python3 migrationDb.py

# finally in admin user
flask run -h 0.0.0.0
```

## Use the API

Endpoints

```
POST person
GET person
DELETE person
PUT person
```

### example with curl

create Jon user
`curl -d "name=Jon&date_of_birth=1989-08-02&job=developer" -X POST http://ec2-18-188-29-88.us-east-2.compute.amazonaws.com:5000/person`

get Jon information
`curl -X GET http://ec2-18-188-29-88.us-east-2.compute.amazonaws.com:5000/person/Jon`

update Jon information
`curl -d "name=Other&date_of_birth=2000-05-05&job=Ing" -X PUT http://localhost:5000/person/Jon`

delete Jon user
`curl -X DELETE http://ec2-18-188-29-88.us-east-2.compute.amazonaws.com:5000/person/Other`


### run it locally

following the `How to run` instructions you can deploy it locally and test replacing
`http://ec2-18-188-29-88.us-east-2.compute.amazonaws.com` with `http://localhost` with the same behaviour

