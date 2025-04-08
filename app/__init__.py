import logging
import logging.config
import os

import yaml
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config_map, log_level_map
from utils.constants import INIT_APP_ENV_MESSAGE, LOGGING_CONFIG_FILE, LOGGING_LOGGER_NAME
from utils.get_config_name import get_config_name

from .routes.auth import auth_bp

db = SQLAlchemy()
migrate = Migrate()


def setup_logging(config_path: str) -> None:
    """
    ロギング設定を適用する

    Args:
        config_path (str): 使用する設定環境
    """

    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)


def create_app(config_name: str | None = None) -> Flask:
    """
    アプリケーションを作成する

    Args:
        config_name (str): 使用する設定環境
        例: "development", "production"など
        flaskコマンドで自動的に呼び出された場合など、
        引数がない場合は環境変数から環境名を取得する

    Returns:
        Flask: 初期化済みFlaskアプリケーションインスタンス
    """

    # 環境ごとの設定
    app = Flask(__name__)
    if config_name is None:
        config_name = get_config_name()
    app.config.from_object(config_map[config_name])

    # ロギング
    setup_logging(LOGGING_CONFIG_FILE)
    app.logger = logging.getLogger(LOGGING_LOGGER_NAME)
    app.logger.setLevel(log_level_map.get(config_name, logging.WARNING))

    app.logger.info(f"{config_name} {INIT_APP_ENV_MESSAGE}")

    # ルート
    app.register_blueprint(auth_bp)

    # データベース関連
    db.init_app(app)
    migrate.init_app(app, db)

    return app
