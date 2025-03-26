from app import db
from utils.datetime_utils import now_jst


class AttendanceReason(db.Model):  # type: ignore
    """
    勤怠理由モデル

    日次勤怠の「理由」項目で選択できる値
    （欠勤、遅刻、早退、遅刻・早退、電車遅延など）
    """

    __tablename__ = "attendance_reasons"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=False, default=now_jst, onupdate=now_jst)
