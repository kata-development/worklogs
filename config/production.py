import os

from dotenv import load_dotenv

from config.config import Config
from utils.constants import DATABASE_URL_MISSING_ERROR, ENV_PRODUCTION_FILE, SECRET_KEY_MISSING_ERROR


class ProductionConfig(Config):
    """
    本番環境用の設定を定義

    Raises:
        RuntimeError: SECRET_KEY が環境変数として設定されていない場合
        RuntimeError: SQLALCHEMY_DATABASE_URI が環境変数として設定されていない場合
    """

    dotenv_path = Config.basedir / ENV_PRODUCTION_FILE
    load_dotenv(dotenv_path)

    DEBUG = False

    SECRET_KEY: str | None = os.environ.get("SECRET_KEY")
    if SECRET_KEY is None:
        raise RuntimeError(SECRET_KEY_MISSING_ERROR)

    SQLALCHEMY_DATABASE_URI: str | None = os.environ.get("SQLALCHEMY_DATABASE_URI")
    if SQLALCHEMY_DATABASE_URI is None:
        raise RuntimeError(DATABASE_URL_MISSING_ERROR)
