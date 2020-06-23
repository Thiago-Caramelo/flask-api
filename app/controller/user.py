from flask import Blueprint
from flask import jsonify
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from app import db
from app.model.user import User
from app.schema.user import UserSchema
from marshmallow import ValidationError

bp = Blueprint("user", __name__, url_prefix='/user')


@bp.route("/", methods=['GET'])
def index():
    """Show all the posts, most recent first."""
    users = User.query.all()
    schema = UserSchema(many=True)
    result = schema.dump(users)
    return jsonify(result.data)


@bp.route("/", methods=["POST"])
def create():
    try:
        user = UserSchema().load(request.get_json())
    except ValidationError as error:
        print(error)
        return error.messages, 400
    else:
        db.session.add(User(name=user.data.name, email=user.data.email))
        db.session.commit()
        return '', 204
