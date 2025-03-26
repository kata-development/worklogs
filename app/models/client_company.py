from datetime import time

from app import db
from utils.datetime_utils import now_jst


class ClientCompany(db.Model):  # type: ignore
    """
    出向先企業モデル

    出向先企業のマスターデータ
    """

    __tablename__ = "client_companies"

    # 企業コード：登録時に管理部が付与する番号
    company_id = db.Column(db.String(100), primary_key=True, nullable=False)
    # 企業名：紐付く勤怠データがある場合は編集不可とする
    name = db.Column(db.String(100), unique=True, nullable=False)
    # 連絡先：住所やメールアドレスや担当者など
    contact = db.Column(db.String(255), nullable=False)

    start_time = db.Column(db.Time, nullable=False, default=time(9, 0))
    end_time = db.Column(db.Time, nullable=False, default=time(18, 0))
    work_unit_id = db.Column(db.Integer, db.ForeignKey("work_units.id"), nullable=False, default=1)

    # 勤務時間外の休憩時間：紐付く勤怠データがある場合は編集不可とする
    morning_break_start = db.Column(db.Time, nullable=True)
    morning_break_end = db.Column(db.Time, nullable=True)
    lunch_break_start = db.Column(db.Time, nullable=True)
    lunch_break_end = db.Column(db.Time, nullable=True)
    evening_break_start = db.Column(db.Time, nullable=True)
    evening_break_end = db.Column(db.Time, nullable=True)
    night_break_start = db.Column(db.Time, nullable=True)
    night_break_end = db.Column(db.Time, nullable=True)
    late_night_break_start = db.Column(db.Time, nullable=True)
    late_night_break_end = db.Column(db.Time, nullable=True)

    # 備考：管理者が記入する備考
    remarks = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=False, default=now_jst, onupdate=now_jst)
    version = db.Column(db.Integer, nullable=False, default=0)
