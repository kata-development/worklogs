"""アプリケーションで使用する定数"""

# 環境変数関連
ENV_FILE = ".env"
ENV_DEVELOPMENT_FILE = ".env.development"
ENV_PRODUCTION_FILE = ".env.production"
ENV_STAGING_FILE = ".env.staging"

# 開発時のシークレットキー
DEVELOPMENT_SECRET_KEY = "development-secret-key"
TESTING_SECRET_KEY = "testing-secret-key"

# SQLiteメモリデータベースURI
SQLITE_MEMORY_DATABASE_URI = "sqlite:///:memory:"

# エラーメッセージ
DATABASE_URI_MISSING_ERROR = "環境変数にDATABASE_URIが登録されていません"
SECRET_KEY_MISSING_ERROR = "環境変数にSECRET_KEYが登録されていません"
