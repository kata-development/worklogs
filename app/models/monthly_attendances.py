from app import db
from utils.datetime_utils import now_jst


class MonthlyAttendance(db.Model):  # type: ignore
    """
    月次勤怠モデル

    社員と出向先企業の中間モデルの拡張
    社員、出向先企業、年、月で一意になる月次の勤怠データ
    """

    __tablename__ = "monthly_attendances"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.employee_id"), nullable=False)
    company_id = db.Column(db.String(100), db.ForeignKey("client_companies.company_id"), nullable=False)

    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)

    # 定期券代：定期券ありの場合は値を入力（0=定期券なし）
    commuter_pass_cost = db.Column(db.Integer, nullable=False, default=0)
    # 作業内容：作業者が記入する作業内容
    description = db.Column(db.String(255), nullable=True)
    # 備考：作業者が記入する備考
    remarks = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=False, default=now_jst, onupdate=now_jst)
    version = db.Column(db.Integer, nullable=False, default=0)

    __table_args__ = (
        db.UniqueConstraint("employee_id", "company_id", "year", "month", name="unique_monthly_attendance"),
        db.CheckConstraint("month >= 1 AND month <= 12", name="check_monthly_attendances_month_range"),
    )
