from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue

from app.forms.auth.login_form import LoginForm

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["GET", "POST"])
def login() -> ResponseReturnValue:
    # TODO: ログイン処理を実装する

    form = LoginForm()

    if form.validate_on_submit():
        pass

    return render_template("auth/login.html", form=form)
