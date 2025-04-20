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

# 項目名のラベル
LABEL_EMPLOYEE_CODE = "社員コード"
LABEL_EMAIL = "メールアドレス"
LABEL_PASSWORD = "パスワード"

# ボタンのラベル
BUTTON_LOGIN = "ログイン"

# メッセージ
MESSAGE_INIT_APP_ENV = "{config} 環境でアプリケーションを初期化しました"

# エラーメッセージ
ERROR_DATABASE_CONFIG = "データベース構成に必要な環境変数が不足しています"
ERROR_SECRET_KEY_MISSING = "環境変数にSECRET_KEYが登録されていません"
ERROR_CONFIG_FILE_NOT_FOUND = "環境設定ファイルが見つかりません"

# 文字
HALF_WIDTH_ALPHANUMERIC_PATTERN = r"^[a-zA-Z0-9]+$"
PASSWORD_SPECIAL_CHARACTERS = "!@#$%^&*()"

# 文字の長さ
PASSWORD_MIN_LENGTH = 16
PASSWORD_MAX_LENGTH = 30
EMAIL_MAX_LENGTH = 255
EMPLOYEE_CODE_MAX_LENGTH = 4

# エラーメッセージのテンプレート
ERROR_REQUIRED = "{field}は必須入力です"
ERROR_LENGTH = "{field}は{length}文字以内で入力してください"
ERROR_LENGTH_RANGE = "{field}は{min_length}文字以上{max_length}文字以下で入力してください"
ERROR_INVALID_FORMAT = "{field}の形式が正しくありません"
ERROR_PASSWORD_COMBINATION = "パスワードはアルファベットの大文字、小文字、数字、記号 {chars} を組み合わせてください"
ERROR_ALPHANUMERIC_ONLY = "{field}は半角英数字のみ使用できます"
ERROR_ALPHANUMERIC_AND_SYMBOLS_ONLY = "{field}は半角英数字と記号 {chars} のみ使用できます"
