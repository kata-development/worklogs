import os
from pathlib import Path

from dotenv import load_dotenv

from utils.constants import ENV_CONFIG_DIR, ENV_FILE, ERROR_CONFIG_FILE_NOT_FOUND


def get_config_name() -> str:
    """設定環境名 (config_name) を取得する

    Returns:
        str: 設定環境名（例: "development", "production" など）
    """
    basedir = Path(__file__).resolve().parent.parent
    dotenv_path = basedir / ENV_CONFIG_DIR / ENV_FILE

    if not dotenv_path.exists():
        raise FileNotFoundError(f"{ERROR_CONFIG_FILE_NOT_FOUND}: {dotenv_path}")

    load_dotenv(dotenv_path, override=True)
    config_name = os.getenv("FLASK_CONFIG", "default")

    return config_name
