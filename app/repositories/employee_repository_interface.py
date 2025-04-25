from abc import ABC, abstractmethod

from app.models.employees import Employee


class EmployeeRepositoryInterface(ABC):
    """社員リポジトリインターフェース"""

    @abstractmethod
    def get_active_employee_by_credentials(self, employee_code: str, email: str) -> Employee | None:
        """有効な社員を社員コードとメールアドレスで取得する

        Args:
            employee_code (str): 社員コード
            email (str): 社員のメールアドレス

        Returns:
            Employee | None: 該当する社員が存在する場合はEmployeeオブジェクト、存在しない場合はNone
        """
        pass

    @abstractmethod
    def get_by_id(self, employee_code: str) -> Employee | None:
        """社員コード（id）で社員を取得する

        Args:
            employee_code (str): 社員コード

        Returns:
            Employee | None: 該当する社員が存在する場合はEmployeeオブジェクト、存在しない場合はNone
        """
        pass
