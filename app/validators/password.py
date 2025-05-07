import string

from wtforms import Form  # type: ignore
from wtforms.fields import Field  # type: ignore
from wtforms.validators import ValidationError  # type: ignore

from utils.constants import (
    ERROR_ALPHANUMERIC_AND_SYMBOLS_ONLY,
    ERROR_PASSWORD_COMBINATION,
    LABEL_PASSWORD,
    PASSWORD_SPECIAL_CHARACTERS,
)


def validate_strong_password(_form: Form, field: Field) -> None:
    """パスワードの構文チェック（英大文字・英小文字・数字・記号）

    WTForms のカスタムバリデータ仕様に従い、_form 引数が必要
    （この関数内では form は使用しないが削除するとエラーになる）

    パスワードはアルファベットの大文字、小文字、数字、許可された記号を
    組み合わせる必要があり、半角英数字と指定された記号のみを使用する
    （記号は定数 utils.constants.PASSWORD_SPECIAL_CHARACTERS に定義）
    例: "Password1234567!" のような形式

    Args:
        _form (Form): フォームオブジェクト
        field (Field): 対象フィールド

    Raises:
        ValidationError: パスワードが無効な場合
    """
    password_data: str = field.data
    allowed_chars: str = string.ascii_letters + string.digits + PASSWORD_SPECIAL_CHARACTERS

    # 英大文字、英小文字、数字、記号のすべてが含まれているかチェック
    if not (
        any(char.isupper() for char in password_data)
        and any(char.islower() for char in password_data)
        and any(char.isdigit() for char in password_data)
        and any(char in PASSWORD_SPECIAL_CHARACTERS for char in password_data)
    ):
        raise ValidationError(ERROR_PASSWORD_COMBINATION.format(chars=PASSWORD_SPECIAL_CHARACTERS))

    # 半角英数字及び指定された記号のみが使用されているかチェック
    if any(char not in allowed_chars for char in password_data):
        raise ValidationError(
            ERROR_ALPHANUMERIC_AND_SYMBOLS_ONLY.format(field=LABEL_PASSWORD, chars=PASSWORD_SPECIAL_CHARACTERS)
        )
