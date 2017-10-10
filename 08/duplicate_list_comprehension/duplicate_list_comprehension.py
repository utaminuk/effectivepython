"""
### 項目8: リスト内包表記は3つ以上の指揮を避ける

- リスト内包表記自体は便利だが重ねると読み解くのが難しくなるので３つ以上の式を避けるようにする。
"""


def get_flat(original: list):
    """
    入力された２重構造のリスト中の数を1重階層のリストに変更して返す

    >>> get_flat([1,2,3],[4,5],[6,7])
    [1,2,3,4,5,6,7]
    """

    return [x for row in original for x in row]


if __name__ == "__main__":
    print(get_flat([1, 2, 3], [4, 5]))