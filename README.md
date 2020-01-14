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

# migrate database into python terminal
python3
from app import db
db.create_all()
exit()

# finally run the project
flask run -h 0.0.0.0
```

## Use the API

It needed a JWT get it from signing up by `sign_up` and `login` endpoints

Example
```sh
curl -H "Content-type: application/json" -d '{"username":"name", "password":"pass"}' -X POST http://localhost:5000/sign_up
curl -H "Content-type: application/json" -d '{"username":"name", "password":"pass"}' -X POST http://localhost:5000/login
```

you will get something like this

```
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Nzg5Nzc5ETIsIm5iZiI6MTU3ODk3Nzk1MiwianRpIjoiOGY2OTY3MDUtZDZmMS00ODBjLThlMWYtOTMzNmY4OWEzN2I4IiwiZXhwIjoxNLc1OTc5ODUyLCJpZGVudGl0eSI6ImpvbiIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.nYUU83KgWiaAUqdy2KW7lm9ai-RN0oLc5OEDnnb5Quo"}

```


Then you can use the following REST endpoints
```
POST person
GET person
DELETE person
PUT person
```

### example with curl

#### 1. create Jon user

`curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLC..." -H "Content-type: application/json" -d '{"name":"Jon", "date_of_birth":"2000-1-1", "job": "dev"}' -X POST http://localhost:5000/person`

#### 2. get Jon information

`curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLC..." -X GET http://localhost:5000/person/1`

#### 3. update Jon information

`curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLC..." -H "Content-type: application/json" -d '{"name":"JonTWO", "date_of_birth":"2020-1-1", "job": "dev"}' -X PUT http://localhost:5000/person/1`

#### 4. delete Jon user

`curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLC..." -X DELETE http://localhost:5000/person/1`


### run in AWS ec2

This service was deployed in an AWS cloud, be free of test it in

`http://ec2-18-188-29-88.us-east-2.compute.amazonaws.com:5000`



