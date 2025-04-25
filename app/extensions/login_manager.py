"""ログインマネージャ初期化モジュール"""

from flask import Flask
from flask_login import LoginManager  # type: ignore

from app.models import Employee
from app.repositories.employee_repository_interface import EmployeeRepositoryInterface
from utils.constants import LOGIN_VIEW

login_manager = LoginManager()


def init_login_manager(app: Flask) -> None:
    """FlaskアプリにLoginManagerを初期化・設定する

    Args:
        app (Flask): Flaskアプリケーションインスタンス
    """
    login_manager.init_app(app)
    login_manager.login_view = LOGIN_VIEW
    repository: EmployeeRepositoryInterface = app.container.employee_repository()  # type: ignore

    @login_manager.user_loader
    def load_user(employee_code: str) -> Employee | None:
        return repository.get_by_id(employee_code)
