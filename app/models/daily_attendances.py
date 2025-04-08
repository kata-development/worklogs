from app import db
from utils.datetime_utils import now_jst


class DailyAttendance(db.Model):  # type: ignore
    """
    日次勤怠モデル

    社員と出向先企業の中間モデルの拡張
    月次勤怠に所属する日次の勤怠データ
    """

    __tablename__ = "daily_attendances"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.employee_id"), nullable=False)
    company_id = db.Column(db.String(100), db.ForeignKey("client_companies.company_id"), nullable=False)

    report_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    # 勤怠理由ID：理由ありの場合のみ入力（欠勤、遅刻、早退、など）
    reason_id = db.Column(db.Integer, db.ForeignKey("attendance_reasons.id"), nullable=True)
    # 有休取得（True/False）
    is_paid_leave = db.Column(db.Boolean, nullable=False, default=False)
    # 時間休開始：時間休の場合のみ入力
    hourly_leave_start = db.Column(db.Time, nullable=True)
    # 時間休終了：時間休の場合のみ入力
    hourly_leave_end = db.Column(db.Time, nullable=True)

    # 訪問先：訪問先がある場合のみ入力
    visiting_place = db.Column(db.String(255), nullable=True)
    # 乗車経路：訪問先がある場合のみ入力
    route = db.Column(db.String(255), nullable=True)
    # 近地旅費金額：訪問先がある場合のみ入力
    travel_expense = db.Column(db.Integer, nullable=True)

    # 在宅勤務（True/False）
    is_telecommuting = db.Column(db.Boolean, nullable=False, default=False)
    # 通勤費実費金額：通勤費がある場合は値を入力（0=なし)
    actual_cost = db.Column(db.Integer, nullable=False, default=0)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=False, default=now_jst, onupdate=now_jst)
    version = db.Column(db.Integer, nullable=False, default=0)

    __table_args__ = (db.UniqueConstraint("employee_id", "company_id", "report_date", name="unique_daily_attendance"),)
