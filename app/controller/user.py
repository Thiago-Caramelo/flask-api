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
from app.schema.user import UserSchema, CreateUserSchema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

bp = Blueprint("user", __name__, url_prefix='/user')


@bp.route("/", methods=['GET'])
def index():
    """Show all the posts, most recent first."""
    users = User.query.all()
    result = UserSchema().dump(users, many=True)
    return jsonify(result.data)


@bp.route("/", methods=["POST"])
def create():
    try:
        user = CreateUserSchema().load(request.get_json())
        new_user = User(name=user.data.name, email=user.data.email)
        db.session.add(new_user)
        db.session.commit()
        db.session.refresh(new_user)
        result = UserSchema().dump(new_user)
        return jsonify(result.data), 201
    except ValidationError as error:
        print(error)
        return error.messages, 400
    except IntegrityError as error:
        print(error)
        return "", 400
