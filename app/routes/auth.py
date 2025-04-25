from dependency_injector.wiring import Provide, inject
from flask import Blueprint, redirect, render_template, url_for
from flask.typing import ResponseReturnValue

from app.containers import Container
from app.forms.auth.login_form import LoginForm
from app.services.auth_service import AuthService
from utils.constants import ERROR_INVALID_CREDENTIALS

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["GET", "POST"])
@inject
def login(auth_service: AuthService = Provide[Container.auth_service]) -> ResponseReturnValue:
    """ログイン画面"""
    form = LoginForm()
    if form.validate_on_submit():
        next_page = auth_service.authenticate_and_login(form.employee_code.data, form.email.data, form.password.data)

        if next_page:
            return redirect(url_for(next_page))

        form.password.errors.append(ERROR_INVALID_CREDENTIALS)

    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@inject
def logout(auth_service: AuthService = Provide[Container.auth_service]) -> ResponseReturnValue:
    """ログアウト処理"""
    auth_service.logout()
    return redirect(url_for("auth.login"))
