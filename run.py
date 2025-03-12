"""
Flaskアプリケーションのエントリポイント

環境変数を読み込み、各環境の設定でFlaskアプリケーションを作成する

Example:
    $ python run.py
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask

from app import create_app
from utils.constants import ENV_FILE

basedir = Path(__file__).resolve().parent
dotenv_path = basedir / ENV_FILE
load_dotenv(dotenv_path)

config_name = os.getenv("FLASK_CONFIG", "default")
app: Flask = create_app(config_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
