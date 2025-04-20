# app/containers.py
from dependency_injector import containers, providers

from app.repositories.employee_repository import EmployeeRepository
from app.services.auth_service import AuthService


class Container(containers.DeclarativeContainer):
    """DIコンテナクラス"""

    # DI対象のワイヤリング
    wiring_config = containers.WiringConfiguration(modules=["app.routes.auth"])

    # Repositoryのプロバイダ
    employee_repository = providers.Singleton(EmployeeRepository)

    # ServiceにRepositoryを注入
    auth_service = providers.Factory(
        AuthService,
        repository=employee_repository,
    )  # type: ignore
