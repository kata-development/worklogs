from app import db
from utils.datetime_utils import now_jst


class Employee(db.Model):  # type: ignore
    """
    社員モデル

    社員情報のマスターデータ
    """

    __tablename__ = "employees"

    # 社員ID：入社時に管理部から発行された4桁の数字
    employee_id = db.Column(db.Integer, primary_key=True, nullable=False)
    # 氏名：姓+名を結合したフルネーム
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # 管理者権限：管理者は管理用メニューが利用可能
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    # 有効状態：有効でない社員はログイン不可
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=False, default=now_jst, onupdate=now_jst)
    version = db.Column(db.Integer, nullable=False, default=0)
