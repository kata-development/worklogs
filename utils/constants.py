"""アプリケーションで使用する定数"""

# 環境変数関連
ENV_FILE = ".env"
ENV_DEVELOPMENT_FILE = ".env.development"
ENV_PRODUCTION_FILE = ".env.production"
ENV_STAGING_FILE = ".env.staging"
ENV_CONFIG_DIR = "config"

# 開発時のシークレットキー
DEVELOPMENT_SECRET_KEY = "development-secret-key"
TESTING_SECRET_KEY = "testing-secret-key"

# データベース関連
DB_DIALECT = "mysql"
DB_DRIVER = "pymysql"
SQLITE_MEMORY_DATABASE_URI = "sqlite:///:memory:"

# ロギング
LOGGING_CONFIG_FILE = "config/logging.yaml"
LOGGING_LOGGER_NAME = "app_logger"

# メッセージ
INIT_APP_ENV_MESSAGE = "環境でアプリケーションを初期化しました"

# エラーメッセージ
DATABASE_CONFIG_ERROR = "データベース構成に必要な環境変数が不足しています"
SECRET_KEY_MISSING_ERROR = "環境変数にSECRET_KEYが登録されていません"
CONFIG_FILE_NOT_FOUND_ERROR = "環境設定ファイルが見つかりません"
