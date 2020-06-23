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

bp = Blueprint("user", __name__, url_prefix='/user')


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    posts = User.query.all()
    schema = UserSchema(many=True)
    result = schema.dump(posts)
    return jsonify(result.data)
