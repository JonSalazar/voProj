from flask import Flask, jsonify, make_response, abort, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token
)
import loginController
from personController import PersonController
import requests

app = Flask(__name__)
app.config.from_object('config')

jwt = JWTManager(app)

person = PersonController()

@app.route('/sign_up', methods=['POST'])
def signUp():
    if not request.is_json:
        return (jsonify({'msg': 'Missing JSON in request'}), 400)

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if (not username):
        return (jsonify({'msg': 'Missing username'}), 400)
    if (not password):
        return (jsonify({'msg': 'Missing password'}), 400)

    if (not loginController.signUp(username, password)):
        return (jsonify({'msg': 'User already registered'}), 400)

    return (jsonify({'msg': 'User registered successfully'}), 200)

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return (jsonify({'msg': 'Missing JSON in request'}), 400)
    
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if (not username):
        return (jsonify({'msg': 'Missing username'}), 400)
    if (not password):
        return (jsonify({'msg': 'Missing password'}), 400)

    if (not loginController.login(username, password)):
        return (jsonify({'msg': 'Bad user or password'}), 400)

    access_token = create_access_token(identity=username)

    return (jsonify({'access_token': access_token}), 200)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/person', methods=['POST'])
@jwt_required
def add_person():
    person.add_person(
        request.form.get('name'),
        request.form.get('date_of_birth'),
        request.form.get('job')
        )
    return jsonify({'status': 'success'})

@app.route('/person/<person_name>', methods=['DELETE'])
@jwt_required
def delete_person(person_name):
    person.delete_person(person_name)
    return jsonify({'status': 'success'})

@app.route('/person/<person_name>', methods=['GET'])
@jwt_required
def get_person(person_name):
    p = person.get_person(person_name)
    return jsonify({'status': 'success', 'value': p})

@app.route('/person/<person_name>', methods=['PUT'])
@jwt_required
def put_person(person_name):
    person.put_person(
        person_name,
        request.form.get('name'),
        request.form.get('date_of_birth'),
        request.form.get('job')
        )
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run()

# curl -d "name=jon&date_of_birth=1989-08-02&job=developer" -X POST http://localhost:5000/person
