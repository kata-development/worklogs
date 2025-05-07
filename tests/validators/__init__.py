from wtforms import Form


class DummyForm(Form):
    """WTformsフォームの検証用クラス"""

    pass


class DummyField:
    """バリデーション対象としてdata 属性を持つ検証用フィールドクラス"""

    def __init__(self, data: str):
        self.data = data
