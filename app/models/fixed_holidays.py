from app import db
from utils.datetime_utils import now_jst


class FixedHoliday(db.Model):  # type: ignore
    """固定祭日モデル

    企業ごとの毎年固定の祭日（例：12/30～1/3は年末年始休暇）
    祭日名または日付の重複を許容する
    """

    __tablename__ = "fixed_holidays"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    company_id = db.Column(db.String(100), db.ForeignKey("client_companies.company_id"), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=False, default=now_jst, onupdate=now_jst)
    version = db.Column(db.Integer, nullable=False, default=0)

    __table_args__ = (
        db.CheckConstraint("month >= 1 AND month <= 12", name="check_fixed_holidays_month_range"),
        db.CheckConstraint("day >= 1 AND day <= 31", name="check_fixed_holidays_day_range"),
    )
