"""
数组array为一维列表，求出现次数最多的元素的值和次数
"""
from typing import Any


def get_most_common_value_and_count(array: list[Any]) -> (Any, int):
    from collections import Counter
    count = Counter(array)
    return count.most_common()[0]


if __name__ == '__main__':
    array = [1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 3, 4, 2, 5, 6]
    print(get_most_common_value_and_count(array))
