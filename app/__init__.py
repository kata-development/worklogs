from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.extensions.blueprints import register_blueprints
from app.extensions.database import init_db
from app.extensions.di import setup_di
from app.extensions.logging import setup_logging
from app.extensions.login_manager import init_login_manager
from app.extensions.migrate import init_migrate
from config import config_map
from utils.constants import MESSAGE_INIT_APP_ENV
from utils.get_config_name import get_config_name

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name: str | None = None) -> Flask:
    """アプリケーションを作成する

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

    # モデル
    from app import models  # noqa: F401

    # ルート
    register_blueprints(app)

    # データベース関連
    init_db(app)
    init_migrate(app)

    # DI設定
    setup_di(app)

    # ログインマネージャ
    init_login_manager(app)

    # ロギング
    app.logger = setup_logging(config_name)
    app.logger.info(MESSAGE_INIT_APP_ENV.format(config=config_name))

    return app
