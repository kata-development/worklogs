from pathlib import Path


class Config:
    """アプリケーションの基本設定"""

    basedir = Path(__file__).resolve().parent

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
