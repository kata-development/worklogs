"""マイグレーション初期化モジュール"""

from flask import Flask
from flask_migrate import Migrate

from app.extensions.database import db

migrate = Migrate()


def init_migrate(app: Flask) -> None:
    """FlaskアプリでMigrateを初期化する

    Args:
        app (Flask): Flaskアプリケーションインスタンス
    """
    migrate.init_app(app, db)
