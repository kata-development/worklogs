"""Blueprint登録モジュール"""

from flask import Flask

from app.routes.auth import auth_bp
from app.routes.errors import errors_bp
from app.routes.main import main_bp


def register_blueprints(app: Flask) -> None:
    """FlaskアプリにBlueprintを登録する

    Args:
        app (Flask): Flaskアプリケーションインスタンス
    """
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)
