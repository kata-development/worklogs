from app import db
from utils.datetime_utils import now_jst


class TeleworkAllowance(db.Model):  # type: ignore
    """
    在宅勤務手当モデル

    在宅勤務手当の金額（出向先企業などに関係なく全社員で共通の金額）
    """

    __tablename__ = "telework_allowances"

    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=False, default=now_jst, onupdate=now_jst)

    __table_args__ = (
        db.PrimaryKeyConstraint("year", "month"),
        db.CheckConstraint("month >= 1 AND month <= 12", name="check_telework_allowances_month_range"),
    )
