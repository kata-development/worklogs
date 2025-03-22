from app import db
from utils.now_jst import now_jst


class VariableHoliday(db.Model):  # type: ignore
    """
    変動祭日モデル

    企業ごとの特定の日の祭日
    祭日名または日付の重複を許容する
    """

    __tablename__ = "variable_holidays"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    company_id = db.Column(db.String(100), db.ForeignKey("client_companies.company_id"), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=True, onupdate=now_jst)
    version = db.Column(db.Integer, nullable=False, default=0)
