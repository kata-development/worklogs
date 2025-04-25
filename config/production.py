import os

from dotenv import load_dotenv

from config.config import Config
from utils.constants import DB_DIALECT, DB_DRIVER, ENV_PRODUCTION_FILE, ERROR_DATABASE_CONFIG, ERROR_SECRET_KEY_MISSING


class ProductionConfig(Config):
    """本番環境用の設定を定義

    Raises:
        RuntimeError: SECRET_KEY が環境変数として設定されていない場合
        RuntimeError: データベース構成に必要な環境変数が不足している場合
    """

    dotenv_path = Config.basedir / ENV_PRODUCTION_FILE
    load_dotenv(dotenv_path, override=True)

    DEBUG = False

    SECRET_KEY = os.getenv("SECRET_KEY")
    if SECRET_KEY is None:
        raise RuntimeError(ERROR_SECRET_KEY_MISSING)

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    if not all([DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME]):
        raise RuntimeError(ERROR_DATABASE_CONFIG)

    SQLALCHEMY_DATABASE_URI = f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
