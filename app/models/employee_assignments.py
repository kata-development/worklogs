from app import db
from utils.datetime_utils import now_jst


class EmployeeAssignment(db.Model):  # type: ignore
    """社員配置モデル

    社員と出向先企業の中間モデルの拡張
    社員の出向先企業を期間（日単位）で登録する
    """

    __tablename__ = "employee_assignments"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    employee_code = db.Column(db.String(100), db.ForeignKey("employees.employee_code"), nullable=False)
    company_code = db.Column(db.String(100), db.ForeignKey("client_companies.company_code"), nullable=False)

    # 開始日：社員の各企業への出向期間は重複しない
    start_date = db.Column(db.Date, nullable=False)
    # 終了日：社員の各企業への出向期間は重複しない・終了日が未定の場合はNULL
    end_date = db.Column(db.Date, nullable=True)

    # 備考：管理者が記入する備考
    remarks = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=False, default=now_jst, onupdate=now_jst)
    version = db.Column(db.Integer, nullable=False, default=0)
