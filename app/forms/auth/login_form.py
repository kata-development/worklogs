from flask_wtf import FlaskForm  # type: ignore
from wtforms import EmailField, PasswordField, StringField, SubmitField  # type: ignore
from wtforms.validators import DataRequired, Email, Length, Regexp  # type: ignore

from app.validators.password import validate_strong_password
from utils.constants import (
    BUTTON_LOGIN,
    EMAIL_MAX_LENGTH,
    EMPLOYEE_CODE_MAX_LENGTH,
    ERROR_ALPHANUMERIC_ONLY,
    ERROR_INVALID_FORMAT,
    ERROR_LENGTH,
    ERROR_LENGTH_RANGE,
    ERROR_REQUIRED,
    HALF_WIDTH_ALPHANUMERIC_PATTERN,
    LABEL_EMAIL,
    LABEL_EMPLOYEE_CODE,
    LABEL_PASSWORD,
    PASSWORD_MAX_LENGTH,
    PASSWORD_MIN_LENGTH,
)


class LoginForm(FlaskForm):
    """ログイン用フォーム

    バリデーション仕様:
    - 社員コード: 半角英数字のみ4文字以内
    - メールアドレス: 標準的なメール形式
    - パスワード: 半角英数字と指定記号の組み合わせ16文字以上30文字以下
    """

    employee_code = StringField(
        LABEL_EMPLOYEE_CODE,
        validators=[
            DataRequired(ERROR_REQUIRED.format(field=LABEL_EMPLOYEE_CODE)),
            Length(
                max=EMPLOYEE_CODE_MAX_LENGTH,
                message=ERROR_LENGTH.format(field=LABEL_EMPLOYEE_CODE, length=EMPLOYEE_CODE_MAX_LENGTH),
            ),
            Regexp(HALF_WIDTH_ALPHANUMERIC_PATTERN, message=ERROR_ALPHANUMERIC_ONLY.format(field=LABEL_EMPLOYEE_CODE)),
        ],
        render_kw={"placeholder": LABEL_EMPLOYEE_CODE, "maxlength": EMPLOYEE_CODE_MAX_LENGTH},
    )
    email = EmailField(
        LABEL_EMAIL,
        validators=[
            DataRequired(ERROR_REQUIRED.format(field=LABEL_EMAIL)),
            Length(max=EMAIL_MAX_LENGTH, message=ERROR_LENGTH.format(field=LABEL_EMAIL, length=EMAIL_MAX_LENGTH)),
            Email(ERROR_INVALID_FORMAT.format(field=LABEL_EMAIL)),
        ],
        render_kw={"placeholder": LABEL_EMAIL, "maxlength": EMAIL_MAX_LENGTH},
    )
    password = PasswordField(
        LABEL_PASSWORD,
        validators=[
            DataRequired(ERROR_REQUIRED.format(field=LABEL_PASSWORD)),
            Length(
                min=PASSWORD_MIN_LENGTH,
                max=PASSWORD_MAX_LENGTH,
                message=ERROR_LENGTH_RANGE.format(
                    field=LABEL_PASSWORD, min_length=PASSWORD_MIN_LENGTH, max_length=PASSWORD_MAX_LENGTH
                ),
            ),
            validate_strong_password,
        ],
        render_kw={"placeholder": LABEL_PASSWORD, "maxlength": PASSWORD_MAX_LENGTH, "autocomplete": "off"},
    )
    submit = SubmitField(BUTTON_LOGIN)
