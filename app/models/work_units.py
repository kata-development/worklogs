from app import db
from utils.datetime_utils import now_jst


class WorkUnit(db.Model):  # type: ignore
    """工数単位モデル

    出向先企業の「工数単位」項目で選択できる値（15分、30分など）
    """

    __tablename__ = "work_units"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    # 分：1以上の値で15、30などが入る
    minute = db.Column(db.Integer, nullable=False, default=15)

    created_at = db.Column(db.DateTime, nullable=False, default=now_jst)
    updated_at = db.Column(db.DateTime, nullable=False, default=now_jst, onupdate=now_jst)

    __table_args__ = (db.CheckConstraint("minute >= 1", name="check_work_units_valid_minute"),)
