from typing import Any

from flask import current_app


def log_error(error_template: str, key_values: dict[str, Any], error: Exception) -> None:
    """エラーログを出力する

    Args:
      error_template (str): エラーメッセージのテンプレート文字列
      key_values (dict[str, Any]): コンテキスト情報を含む辞書
      error (Exception): キャッチした例外オブジェクト
    """
    current_app.logger.error(error_template.format(key_values=key_values, error=error))
