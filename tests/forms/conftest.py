# tests/conftest.py
import pytest

from app import create_app


@pytest.fixture
def app():
    """フォームテスト用のテーブルなしFlaskアプリケーションを作成"""
    app = create_app("testing")
    return app


@pytest.fixture(autouse=True)
def db_session():
    """テーブルを使用しない場合のダミーdb_sessionフィクスチャ"""
    yield
