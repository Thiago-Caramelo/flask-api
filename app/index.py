from flask import Flask, jsonify, request
from app.model.user import User, UserSchema

app = Flask(__name__)

incomes = [
    User('Don', 'don56634@gmail.com'),
    User('Dona', 'dona90978787@gmail.com'),
]


@app.route('/incomes')
def get_incomes():
    schema = UserSchema(many=True)
    result = schema.dump(incomes)
    return jsonify(result.data)


@app.route('/incomes', methods=['POST'])
def add_income():
    user = UserSchema().load(request.get_json())
    incomes.append(user.data)
    return '', 204
