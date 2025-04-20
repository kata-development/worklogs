from flask import current_app
from sqlalchemy.exc import SQLAlchemyError

from app.models.employees import Employee
from app.repositories.employee_repository_interface import EmployeeRepositoryInterface
from utils.constants import ERROR_DATABASE


class EmployeeRepository(EmployeeRepositoryInterface):
    """社員リポジトリ"""

    def get_active_employee_by_credentials(self, employee_code: str, email: str) -> Employee | None:
        """有効な社員を社員IDとメールアドレスで取得する

        Args:
            employee_code (str): 社員コード
            email (str): 社員のメールアドレス

        Returns:
            Employee | None: 該当する社員が存在する場合はEmployeeオブジェクト、存在しない場合はNone
        """
        try:
            return Employee.query.filter_by(employee_code=employee_code, email=email, is_active=True).first()

        except SQLAlchemyError as e:
            key_values = {"employee_code": employee_code, "email": email, "is_active": True}
            current_app.logger.error(ERROR_DATABASE.format(key_values=key_values, error=e))
            raise

    def get_by_id(self, employee_code: str) -> Employee | None:
        """社員コードで社員を取得する

        Args:
            employee_code (int): 社員コード

        Returns:
            Employee | None: 該当する社員が存在する場合はEmployeeオブジェクト、存在しない場合はNone
        """
        try:
            return Employee.query.filter_by(employee_code=employee_code).first()

        except SQLAlchemyError as e:
            key_values = {"employee_code": employee_code}
            current_app.logger.error(ERROR_DATABASE.format(key_values=key_values, error=e))
            raise
