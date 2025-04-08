from flask import Blueprint, current_app, render_template
from flask.typing import ResponseReturnValue
from werkzeug.exceptions import HTTPException, InternalServerError, NotFound

errors_bp = Blueprint("errors", __name__)


@errors_bp.app_errorhandler(NotFound)
def handle_not_found_error(e: HTTPException) -> ResponseReturnValue:
    """404エラー（Not Found）"""
    current_app.logger.info(e)
    return render_template("errors/404.html"), 404


@errors_bp.app_errorhandler(InternalServerError)
def handle_internal_server_error(e: HTTPException) -> ResponseReturnValue:
    """500エラー（Internal Server Error）"""
    current_app.logger.exception(e)
    return render_template("errors/500.html"), 500


@errors_bp.app_errorhandler(Exception)
def handle_generic_error(e: Exception) -> ResponseReturnValue:
    """キャッチできなかった全てのエラー
    未定義のエラーは500エラーとして扱う
    """
    current_app.logger.exception(e)
    return render_template("errors/generic_error.html"), 500
