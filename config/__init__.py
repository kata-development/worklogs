"""アプリケーションの設定クラスを管理するモジュール"""

from typing import Type

from config.config import Config
from config.development import DevelopmentConfig
from config.production import ProductionConfig
from config.staging import StagingConfig
from config.testing import TestingConfig

config_map: dict[str, Type[Config]] = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "staging": StagingConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
