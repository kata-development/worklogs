import os

from dotenv import load_dotenv

from config.config import Config
from utils.constants import DATABASE_CONFIG_ERROR, DB_DIALECT, DB_DRIVER, DEVELOPMENT_SECRET_KEY, ENV_DEVELOPMENT_FILE


class DevelopmentConfig(Config):
    """
    開発環境用の設定を定義

    Raises:
        RuntimeError: データベース構成に必要な環境変数が不足している場合
    """

    dotenv_path = Config.basedir / ENV_DEVELOPMENT_FILE
    load_dotenv(dotenv_path)

    DEBUG = True
    SECRET_KEY = DEVELOPMENT_SECRET_KEY

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    if not all([DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME]):
        raise RuntimeError(DATABASE_CONFIG_ERROR)

    SQLALCHEMY_DATABASE_URI = f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
