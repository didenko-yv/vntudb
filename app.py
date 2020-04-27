import sys

sys.path.append('..')
print(sys.path)

from flask import request
from core.tools import wrap_response

from core.config import app, url_prefix
from core.fee import Fee
from core.country import Country
from core.program import Program
from core.partner import Partner
from core.student import Student
from core.require import Require
from core.organization import Organization
from core.college import College

@app.route('/', methods=['GET'])
def hello():
    return wrap_response({"result": "Good"})


@app.route('/colleges', methods=['POST', 'GET', 'PUT', 'DELETE'])
def college():
    result = []
    data = request.json
    args = request.args

    if request.method == 'POST':
        if data:
            result = College.add_to_db(data)
    if request.method == 'GET':
        result = College.get_all()

    if request.method == 'PUT':
        if data:
            result = College.update_by_id(data)

    if request.method == 'DELETE':
        if 'id' in args:
            result = College.delete_by_id(args['id'])

    return wrap_response({"data": result}, False, 200)


@app.route('/organizations', methods=['POST', 'GET', 'PUT', 'DELETE'])
def organization():
    result = []
    data = request.json
    args = request.args

    if request.method == 'POST':
        if data:
            result = Organization.add_to_db(data)

    if request.method == 'GET':
        result = Organization.get_all()

    if request.method == 'PUT':
        if data:
            result = Organization.update_by_id(data)

    if request.method == 'DELETE':
        if 'id' in args:
            result = Organization.delete_by_id(args['id'])

    return wrap_response({"data": result}, False, 200)


@app.route('/fees', methods=['POST', 'GET', 'PUT', 'DELETE'])
def fee():
    result = []
    data = request.json
    args = request.args

    if request.method == 'POST':
        if data:
            result = Fee.add_to_db(data)
    if request.method == 'GET':
        result = Fee.get_all()

    if request.method == 'PUT':
        if data:
            result = Fee.update_by_id(data)

    if request.method == 'DELETE':
        if 'id' in args:
            result = Fee.delete_by_id(args['id'])

    return wrap_response({"data": result}, False, 200)


@app.route('/requires', methods=['POST', 'GET', 'PUT', 'DELETE'])
def require():
    result = []
    data = request.json
    args = request.args

    if request.method == 'POST':
        if data:
            result = Require.add_to_db(data)
    if request.method == 'GET':
        result = Require.get_all()

    if request.method == 'PUT':
        if data:
            result = Require.update_by_id(data)

    if request.method == 'DELETE':
        if 'id' in args:
            result = Require.delete_by_id(args['id'])

    return wrap_response({"data": result}, False, 200)


@app.route('/students', methods=['POST', 'GET', 'PUT', 'DELETE'])
def student():
    result = []
    data = request.json
    args = request.args

    if request.method == 'POST':
        if data:
            result = Student.add_to_db(data)
    if request.method == 'GET':
        result = Student.get_all()

    if request.method == 'PUT':
        if data:
            result = Student.update_by_id(data)

    if request.method == 'DELETE':
        if 'id' in args:
            result = Student.delete_by_id(args['id'])

    return wrap_response({"data": result}, False, 200)


@app.route('/program', methods=['POST', 'GET', 'PUT', 'DELETE'])
def programs():
    result = []
    data = request.json
    args = request.args

    if request.method == 'POST':
        if data:
            result = Program.add_to_db(data)
    if request.method == 'GET':
        result = Program.get_all()

    if request.method == 'PUT':
        if data:
            result = Program.update_by_id(data)

    if request.method == 'DELETE':
        if 'id' in args:
            result = Program.delete_by_id(args['id'])

    return wrap_response({"data": result}, False, 200)


@app.route('/partners', methods=['POST', 'GET', 'PUT', 'DELETE'])
def partner():
    result = []
    data = request.json
    args = request.args

    if request.method == 'POST':
        if data:
            result = Partner.add_to_db(data)
    if request.method == 'GET':
        result = Partner.get_all()

    if request.method == 'PUT':
        if data:
            result = Partner.update_by_id(data)

    if request.method == 'DELETE':
        if 'id' in args:
            result = Partner.delete_by_id(args['id'])

    return wrap_response({"data": result}, False, 200)


@app.route('/countries', methods=['POST', 'GET', 'PUT', 'DELETE'])
def country():
    result = []
    data = request.json
    args = request.args

    if request.method == 'POST':
        if data:
            result = Country.add_to_db(data)

    if request.method == 'GET':
        result = Country.get_all()

    if request.method == 'PUT':
        if data:
            result = Country.update_by_id(data)

    if request.method == 'DELETE':
        if 'id' in args:
            result = Country.delete_by_id(args['id'])

    return wrap_response({"data": result}, False, 200)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5089)