"""ロギング設定モジュール"""

import logging
import logging.config
import os

import yaml

from config import log_level_map
from utils.constants import LOGGING_CONFIG_FILE, LOGGING_LOGGER_NAME


def setup_logging(config_name: str, config_path: str = LOGGING_CONFIG_FILE) -> logging.Logger:
    """ロギング設定を適用し、アプリケーション用のロガーを返す

    Args:
        config_name (str): 使用する設定環境（例: "development"）
        config_path (str): YAML形式のロギング設定ファイルパス

    Returns:
        logging.Logger: アプリケーションロガー
    """
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger(LOGGING_LOGGER_NAME)
    logger.setLevel(log_level_map.get(config_name, logging.WARNING))

    return logger
