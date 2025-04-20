from flask import current_app
from flask_login import current_user, login_user, logout_user  # type: ignore
from werkzeug.security import check_password_hash

from app.models.employees import Employee
from app.repositories.employee_repository_interface import EmployeeRepositoryInterface
from utils.constants import ERROR_AUTHENTICATE_LOGIN, LOGIN_REDIRECT_VIEW, MESSAGE_LOGIN, MESSAGE_LOGOUT


class AuthService:
    """認証サービス"""

    def __init__(self, repository: EmployeeRepositoryInterface):
        self.repository = repository

    def login(self, employee: Employee) -> None:
        """ログイン処理（セッションの開始）

        Args:
            employee (Employee): 認証済みの社員
        """

        login_user(employee)
        current_app.logger.info(MESSAGE_LOGIN.format(user=current_user))

    def logout(self) -> None:
        """ログアウト処理"""

        current_app.logger.info(MESSAGE_LOGOUT.format(user=current_user))
        logout_user()

    def authenticate(self, employee_code: str, email: str, password: str) -> Employee | None:
        """認証処理

        Args:
            employee_code (str): 社員コード
            email (str): メールアドレス
            password (str): 入力されたパスワード

        Returns:
            Employee | None: 認証成功時はEmployeeオブジェクト、失敗時はNone
        """

        employee = self.repository.get_active_employee_by_credentials(employee_code, email)
        if employee and check_password_hash(pwhash=employee.password_hash, password=password):
            return employee

        return None

    def authenticate_and_login(self, employee_code: str, email: str, password: str) -> str | None:
        """社員を認証し、成功した場合はログインを行う

        Args:
            employee_code (str): 認証対象の社員コード
            email (str): 認証対象の社員メールアドレス
            password (str): 認証時のプレーンパスワード

        Returns:
            str | None: 認証とログインが成功した場合、リダイレクト先のエンドポイントを返す
                        認証失敗時はNoneを返す

        Raises:
            Exception: 認証またはログイン処理で予期しないエラーが発生した場合
        """

        try:
            employee = self.authenticate(employee_code, email, password)

            if employee:
                self.login(employee)

                return LOGIN_REDIRECT_VIEW

            return None

        except Exception as e:
            current_app.logger.error(ERROR_AUTHENTICATE_LOGIN.format(error=e))

            raise
