# app/di.py

from flask import Flask

from app.containers import Container


def setup_di(app: Flask) -> None:
    """DIコンテナをセットアップして Flask アプリに統合する

    Args:
        app (Flask): Flask アプリケーションインスタンス
    """
    container = Container()
    app.container = container  # type: ignore
