"""
Flaskアプリケーションのエントリポイント

環境変数を読み込み、各環境の設定でFlaskアプリケーションを作成する

Example:
    $ python run.py
"""

from flask import Flask

from app import create_app
from utils.get_config_name import get_config_name

config_name = get_config_name()
app: Flask = create_app(config_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
