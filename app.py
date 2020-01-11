from flask import Flask, jsonify, make_response, abort, request
from personController import PersonController
import requests

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

person = PersonController()

@app.route('/person', methods=['POST'])
def add_person():
    person.add_person(
        request.form.get('name'),
        request.form.get('date_of_birth'),
        request.form.get('job')
        )
    return jsonify({'status': 'success'})

@app.route('/person/<person_name>', methods=['DELETE'])
def delete_person(person_name):
    person.delete_person(person_name)
    return jsonify({'status': 'success'})

@app.route('/person/<person_name>', methods=['GET'])
def get_person(person_name):
    p = person.get_person(person_name)
    return jsonify({'status': 'success', 'value': p})

@app.route('/person/<person_name>', methods=['PUT'])
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
