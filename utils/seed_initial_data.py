"""
シードデータ登録スクリプト
使い方：プロジェクトルートで以下のコマンドを実行
$ PYTHONPATH=${PWD} python utils/seed_initial_data.py
"""

from flask import Flask

from app import create_app, db
from app.models.attendance_reasons import AttendanceReason
from app.models.telework_allowances import TeleworkAllowance
from app.models.work_units import WorkUnit
from utils.get_config_name import get_config_name


def seed_work_units() -> None:
    """工数単位モデルのシードデータを登録"""

    # 出向先企業の外部キー「工数単位ID」にデフォルト1を設定しているため、
    # id=1のデータを必須として登録する
    id_1 = WorkUnit.query.filter_by(id=1).first()
    if not id_1:
        db.session.add(WorkUnit(id=1, minute=15))

    # id=1以外のデータを登録
    units = [30, 60]
    for unit in units:
        existing = WorkUnit.query.filter_by(minute=unit).first()
        if not existing:
            db.session.add(WorkUnit(minute=unit))


def seed_attendance_reasons() -> None:
    """勤怠理由モデルのシードデータを登録"""

    names = ["欠勤", "遅刻", "早退", "遅刻・早退", "電車遅延", "特別休暇", "災害遅延", "災害遅・早", "時差出勤"]
    for name in names:
        existing = AttendanceReason.query.filter_by(name=name).first()
        if not existing:
            db.session.add(AttendanceReason(name=name))


def seed_telework_allowances() -> None:
    """在宅勤務手当モデルのシードデータを登録"""

    allowances = [
        {"year": 2024, "month": 4, "amount": 5000},
    ]
    for allowance in allowances:
        existing = TeleworkAllowance.query.filter_by(year=allowance["year"], month=allowance["month"]).first()
        if not existing:
            db.session.add(
                TeleworkAllowance(year=allowance["year"], month=allowance["month"], amount=allowance["amount"])
            )


def seed_all() -> None:
    """すべてのシードデータを登録"""

    try:
        seed_work_units()
        seed_attendance_reasons()
        seed_telework_allowances()
        db.session.commit()
        print("シードデータを登録しました")
    except Exception as e:
        db.session.rollback()
        print(f"シードデータ登録エラー: {e}")


if __name__ == "__main__":
    config_name = get_config_name()
    app: Flask = create_app(config_name)

    with app.app_context():
        seed_all()
