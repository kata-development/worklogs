from config.config import Config
from utils.constants import SQLITE_MEMORY_DATABASE_URI, TESTING_SECRET_KEY


class TestingConfig(Config):
    """テスト環境用の設定を定義"""

    DEBUG = True
    TESTING = True
    SECRET_KEY = TESTING_SECRET_KEY
    SQLALCHEMY_DATABASE_URI = SQLITE_MEMORY_DATABASE_URI

    # CSRFを無効化して、フォームの生成を簡易にする
    WTF_CSRF_ENABLED = False
