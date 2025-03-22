from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config_map

from .routes.auth import auth_bp

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name: str) -> Flask:
    """
    アプリケーションを作成する

    Args:
        config_name (str): 使用する設定環境
        例: "development", "production"など

    Returns:
        Flask: 初期化済みFlaskアプリケーションインスタンス
    """

    app = Flask(__name__)
    app.config.from_object(config_map[config_name])

    with app.app_context():
        from app import models  # noqa: F401

    app.register_blueprint(auth_bp)

    db.init_app(app)
    migrate.init_app(app, db)

    return app
