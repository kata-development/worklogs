import pytest
from sqlalchemy.orm import scoped_session, sessionmaker

from app import create_app
from app.extensions.database import db


@pytest.fixture(scope="session")
def app():
    """テスト用の Flask アプリケーションを作成"""
    app = create_app("testing")

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(scope="function")
def client(app):
    """Flask のテストクライアント"""
    return app.test_client()


@pytest.fixture(autouse=True)
def db_session(app):
    """各テストごとにデータベースの状態を初期化するためのフィクスチャ

    Flask‑SQLAlchemy 3.x 以降では `create_scoped_session` は廃止されているため、
    SQLAlchemy 標準の sessionmaker と scoped_session を用いて新たなセッションを生成する
    """
    connection = db.engine.connect()
    transaction = connection.begin()

    # SQLAlchemy の標準APIを使用して scoped_session を生成
    session_factory = sessionmaker(bind=connection)
    session = scoped_session(session_factory)

    # アプリケーション全体で使用するセッションを上書き
    db.session = session

    yield session

    session.remove()
    transaction.rollback()
    connection.close()
