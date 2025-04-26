import random

import pytest
from wtforms.validators import ValidationError

from app.validators.password import validate_strong_password
from tests.validators import DummyField, DummyForm
from utils.constants import (
    ERROR_ALPHANUMERIC_AND_SYMBOLS_ONLY,
    ERROR_PASSWORD_COMBINATION,
    LABEL_PASSWORD,
    PASSWORD_SPECIAL_CHARACTERS,
)

# 有効なパスワード例：英大文字・英小文字・数字・記号が含まれる
valid_password = "Password0123456" + random.choice(PASSWORD_SPECIAL_CHARACTERS)
# パスワードの文字の組み合わせエラーメッセージ
password_compination_error_message = ERROR_PASSWORD_COMBINATION.format(chars=PASSWORD_SPECIAL_CHARACTERS)


@pytest.mark.parametrize(
    "desc, password, expected_error",
    [
        (
            "missing uppercase",
            valid_password.lower(),  # すべて小文字：大文字なし
            password_compination_error_message,
        ),
        (
            "missing lowercase",
            valid_password.upper(),  # すべて大文字：小文字なし
            password_compination_error_message,
        ),
        (
            "missing digit",
            "PasswordTestVal" + random.choice(PASSWORD_SPECIAL_CHARACTERS),  # 数字なし
            password_compination_error_message,
        ),
        (
            "missing symbol",
            "Password01234567",  # 記号なし
            password_compination_error_message,
        ),
    ],
)
def test_invalid_password_components(desc, password, expected_error):
    """英大文字、英小文字、数字、記号のうち少なくとも一つが欠落している場合のエラーが発生すること"""
    field = DummyField(password)
    with pytest.raises(ValidationError) as excinfo:
        validate_strong_password(DummyForm(), field)
    assert str(excinfo.value) == expected_error, f"パスワード検証失敗ケース: {desc}"


def test_invalid_characters():
    """パスワードに許可されていない文字（例：スペース）が含まれる場合のエラーが発生すること"""
    invalid_password = valid_password + " "  # スペースを追加
    field = DummyField(invalid_password)
    expected_error = ERROR_ALPHANUMERIC_AND_SYMBOLS_ONLY.format(
        field=LABEL_PASSWORD, chars=PASSWORD_SPECIAL_CHARACTERS
    )
    with pytest.raises(ValidationError) as excinfo:
        validate_strong_password(DummyForm(), field)
    assert str(excinfo.value) == expected_error


def test_valid_password():
    """すべての必須要素（英大文字・英小文字・数字・記号）が含まれる有効なパスワードの場合エラーが発生しないこと"""
    field = DummyField(valid_password)
    try:
        validate_strong_password(DummyForm(), field)  # 例外が発生しなければ成功
    except ValidationError as e:
        pytest.fail(f"パスワードのバリデーション失敗: {e}")
