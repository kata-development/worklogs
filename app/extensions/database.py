"""データベース初期化モジュール"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app: Flask) -> None:
    """FlaskアプリでSQLAlchemyを初期化する

    Args:
        app (Flask): Flaskアプリケーションインスタンス
    """
    db.init_app(app)
