"""アプリケーションの設定クラスなどを管理するモジュール"""

import logging
from typing import Type

from config.config import Config
from config.development import DevelopmentConfig
from config.production import ProductionConfig
from config.staging import StagingConfig
from config.testing import TestingConfig

# 環境ごとの設定クラスのマッピング
config_map: dict[str, Type[Config]] = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "staging": StagingConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}

# ログレベルのマッピング
log_level_map: dict[str, int] = {
    "development": logging.DEBUG,
    "production": logging.INFO,
    "staging": logging.INFO,
    "testing": logging.INFO,
}
