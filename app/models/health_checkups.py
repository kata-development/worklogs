from app import db
from utils.datetime_utils import now_jst


class HealthCheckup(db.Model):  # type: ignore
    """健康診断受診モデル

    社員ごとに健康診断受診日と受診料を登録する
    """

    __tablename__ = "health_checkups"

    employee_id = db.Column(db.Integer, db.ForeignKey("employees.employee_id"), nullable=False)
    checkup_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=False, default=now_jst, onupdate=now_jst)
    version = db.Column(db.Integer, nullable=False, default=0)

    __table_args__ = (db.PrimaryKeyConstraint("employee_id", "checkup_date"),)
