from flask import Flask, jsonify, request
from app.model.user import User, UserSchema
from marshmallow import ValidationError

app = Flask(__name__)

incomes = [
    User('Don', 'don56634@gmail.com'),
    User('Dona', 'dona90978787@gmail.com'),
]


@app.route('/incomes')
def get_incomes():
    schema = UserSchema(many=True)
    result = schema.dump(incomes)
    return jsonify(result)


@app.route('/incomes', methods=['POST'])
def add_income():
    try:
        user = UserSchema().load(request.get_json())
    except ValidationError as error:
        print(error)
        return error.messages, 400
    else:
        incomes.append(user.data)
        return '', 204
