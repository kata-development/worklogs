# tests/forms/test_login_form.py
import random

import pytest

from app.forms.auth.login_form import LoginForm
from app.validators.password import validate_strong_password
from utils.constants import (
    EMAIL_MAX_LENGTH,
    EMPLOYEE_CODE_MAX_LENGTH,
    ERROR_ALPHANUMERIC_ONLY,
    ERROR_INVALID_FORMAT,
    ERROR_LENGTH,
    ERROR_LENGTH_RANGE,
    ERROR_REQUIRED,
    LABEL_EMAIL,
    LABEL_EMPLOYEE_CODE,
    LABEL_PASSWORD,
    PASSWORD_MAX_LENGTH,
    PASSWORD_MIN_LENGTH,
    PASSWORD_SPECIAL_CHARACTERS,
)


@pytest.fixture
def valid_form_data():
    """有効なログインフォームのデータ"""
    return {
        "employee_code": "1234",
        "email": "user@example.com",
        "password": "ValidPass012345" + random.choice(PASSWORD_SPECIAL_CHARACTERS),
    }


def test_login_form_valid(app, valid_form_data):
    """正常なデータの場合、フォームが valid になること"""
    with app.test_request_context(method="POST", data=valid_form_data):
        form = LoginForm()
        assert form.validate()


def test_employee_code_required(app, valid_form_data):
    """社員コードが必須であること"""
    data = valid_form_data.copy()
    data["employee_code"] = ""
    with app.test_request_context(method="POST", data=data):
        form = LoginForm()
        valid = form.validate()
        assert not valid
        # エラーメッセージ
        expected_error = ERROR_REQUIRED.format(field=LABEL_EMPLOYEE_CODE)
        assert expected_error in form.employee_code.errors


def test_employee_code_length(app, valid_form_data):
    """社員コードの長さが上限を超えている場合エラーが発生すること"""
    data = valid_form_data.copy()
    data["employee_code"] = "1" * (EMPLOYEE_CODE_MAX_LENGTH + 1)
    with app.test_request_context(method="POST", data=data):
        form = LoginForm()
        valid = form.validate()
        assert not valid
        # エラーメッセージ
        expected_error = ERROR_LENGTH.format(field=LABEL_EMPLOYEE_CODE, length=EMPLOYEE_CODE_MAX_LENGTH)
        assert expected_error in form.employee_code.errors


def test_employee_code_non_alphanumeric(app, valid_form_data):
    """社員コードに許可されていない文字が含まれている場合エラーが発生すること"""
    data = valid_form_data.copy()
    data["employee_code"] = "Aa1#"  # 英大文字小文字数字以外の文字を含む
    with app.test_request_context(method="POST", data=data):
        form = LoginForm()
        valid = form.validate()
        assert not valid
        # エラーメッセージ
        expected_error = ERROR_ALPHANUMERIC_ONLY.format(field=LABEL_EMPLOYEE_CODE)
        assert expected_error in form.employee_code.errors


def test_email_required(app, valid_form_data):
    """メールアドレスが必須であること"""
    data = valid_form_data.copy()
    data["email"] = ""
    with app.test_request_context(method="POST", data=data):
        form = LoginForm()
        valid = form.validate()
        assert not valid
        # エラーメッセージ
        expected_error = ERROR_REQUIRED.format(field=LABEL_EMAIL)
        assert expected_error in form.email.errors


def test_email_invalid_format(app, valid_form_data):
    """メールアドレスのフォーマットが不正な場合エラーが発生すること"""
    data = valid_form_data.copy()
    data["email"] = "invalidemail"
    with app.test_request_context(method="POST", data=data):
        form = LoginForm()
        valid = form.validate()
        assert not valid
        # エラーメッセージ
        expected_error = ERROR_INVALID_FORMAT.format(field=LABEL_EMAIL)
        assert expected_error in form.email.errors


def test_email_length(app, valid_form_data):
    """メールアドレスが最大長を超えた場合エラーが発生すること"""
    data = valid_form_data.copy()
    data["email"] = ("a" * (EMAIL_MAX_LENGTH)) + "@example.com"
    with app.test_request_context(method="POST", data=data):
        form = LoginForm()
        valid = form.validate()
        assert not valid
        # エラーメッセージ
        expected_error = ERROR_LENGTH.format(field=LABEL_EMAIL, length=EMAIL_MAX_LENGTH)
        assert expected_error in form.email.errors


def test_password_required(app, valid_form_data):
    """パスワードが必須であること"""
    data = valid_form_data.copy()
    data["password"] = ""
    with app.test_request_context(method="POST", data=data):
        form = LoginForm()
        valid = form.validate()
        assert not valid
        # エラーメッセージ
        expected_error = ERROR_REQUIRED.format(field=LABEL_PASSWORD)
        assert expected_error in form.password.errors


def test_password_length_too_short(app, valid_form_data):
    """パスワードの長さが短い場合エラーが発生すること"""
    data = valid_form_data.copy()
    data["password"] = "a" * (PASSWORD_MIN_LENGTH - 1)
    with app.test_request_context(method="POST", data=data):
        form = LoginForm()
        valid = form.validate()
        assert not valid
        # エラーメッセージ
        expected_error = ERROR_LENGTH_RANGE.format(
            field=LABEL_PASSWORD, min_length=PASSWORD_MIN_LENGTH, max_length=PASSWORD_MAX_LENGTH
        )
        assert expected_error in form.password.errors


def test_password_length_too_long(app, valid_form_data):
    """パスワードの長さが長い場合エラーが発生すること"""
    data = valid_form_data.copy()
    data["password"] = "a" * (PASSWORD_MAX_LENGTH + 1)
    with app.test_request_context(method="POST", data=data):
        form = LoginForm()
        valid = form.validate()
        assert not valid
        # エラーメッセージ
        expected_error = ERROR_LENGTH_RANGE.format(
            field=LABEL_PASSWORD, min_length=PASSWORD_MIN_LENGTH, max_length=PASSWORD_MAX_LENGTH
        )
        assert expected_error in form.password.errors


def test_custom_validator_integration(app, valid_form_data):
    """カスタムバリデータ validate_strong_password が LoginForm に組み込まれていること"""
    data = valid_form_data.copy()
    with app.test_request_context(method="POST", data=data):
        form = LoginForm()
        password_validators = form.password.validators
        assert any(validator == validate_strong_password for validator in password_validators), (
            "カスタムバリデータvalidate_strong_passwordがpasswordフィールドに組み込まれていません"
        )
