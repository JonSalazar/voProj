from flask import Flask, jsonify, make_response, abort, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_sqlalchemy import SQLAlchemy

import requests

app = Flask(__name__)
app.config.from_object('config')

jwt = JWTManager(app)
db = SQLAlchemy(app)

import loginController
import personController

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
    if not request.is_json:
        return (jsonify({'msg': 'Missing JSON in request'}), 400)

    name = request.json.get('name')
    date_of_birth = request.json.get('date_of_birth')
    job = request.json.get('job')

    if (not name):
        return (jsonify({'msg': 'Missing name'}), 400)
    if (not date_of_birth):
        return (jsonify({'msg': 'Missing date_of_birth'}), 400)
    if (not job):
        return (jsonify({'msg': 'Missing job'}), 400)

    id = personController.addPerson(name, date_of_birth, job)

    if (not id):
        return (jsonify({'msg': 'Bad format arguments'}), 422)

    return jsonify({'status': 'success', 'id': id})

@app.route('/person/<int:id>', methods=['DELETE'])
@jwt_required
def delete_person(id):
    result = personController.deletePerson(id)
    if (not result):
        abort(404)

    return jsonify({'status': 'success'})

@app.route('/person/<int:id>', methods=['GET'])
@jwt_required
def get_person(id):
    persona = personController.getPerson(id)
    if (not persona):
        abort(404)

    return jsonify({'status': 'success', 'person': {
        'name': persona.nombre,
        'date_of_birth': persona.fecha_nacimiento,
        'job': persona.puesto
    }})

@app.route('/person/<int:id>', methods=['PUT'])
@jwt_required
def put_person(id):
    if not request.is_json:
        return (jsonify({'msg': 'Missing JSON in request'}), 400)
    
    result = personController.putPerson(
        id,
        request.json.get('name'),
        request.json.get('date_of_birth'),
        request.json.get('job')
    )

    if (not result):
        abort(404)

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run()

# curl -d "name=jon&date_of_birth=1989-08-02&job=developer" -X POST http://localhost:5000/person
