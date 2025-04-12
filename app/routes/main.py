from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def top_menu() -> ResponseReturnValue:
    """トップメニュー画面"""
    return render_template("top_menu.html")
