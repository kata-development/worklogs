from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue
from flask_login import login_required  # type: ignore

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
@login_required
def top_menu() -> ResponseReturnValue:
    """トップメニュー画面"""
    return render_template("top_menu.html")
