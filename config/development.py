import os

from dotenv import load_dotenv

from config.config import Config
from utils.constants import DATABASE_URI_MISSING_ERROR, DEVELOPMENT_SECRET_KEY, ENV_DEVELOPMENT_FILE


class DevelopmentConfig(Config):
    """
    開発環境用の設定を定義

    Raises:
        RuntimeError: SQLALCHEMY_DATABASE_URI が環境変数として設定されていない場合
    """

    dotenv_path = Config.basedir / ENV_DEVELOPMENT_FILE
    load_dotenv(dotenv_path)

    DEBUG = True
    SECRET_KEY = DEVELOPMENT_SECRET_KEY

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    if SQLALCHEMY_DATABASE_URI is None:
        raise RuntimeError(DATABASE_URI_MISSING_ERROR)
