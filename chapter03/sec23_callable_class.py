"""
項目23: クラス型ではなく関数型で単純なインターフェースでシンプルに

Accept Functions for Simple Interfaces Instead of Classes

- 
"""


class CountMissing(object):
    """
    内部カウントをするためのクラス
    """

    def __init__(self):
        """
        コンストラクタ
        """
        self.added = 0

    def __call__(self):
        """
        関数として呼ばれた場合の処理
        added をインクリメントする
        """
        self.added += 1
        return 0


if __name__ == "__main__":
    pass
