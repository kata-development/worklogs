from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/", methods=["GET"])
def login() -> ResponseReturnValue:
    return render_template("auth/login.html")
