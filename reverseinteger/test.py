import pytest

from reverseinteger.solution import Solution


@pytest.mark.parametrize("input, expected", [
    [0, 0],
    [1, 1],
    [-1, -1],
    [10, 1],
    [-10, -1],
    [100, 1],
    [-100, -1],
    [123, 321],
    [-123, -321],
    [120, 21],
    [1534236469, 0],
])
def test_reverse_integer(input: int, expected: int):
    solution = Solution()
    assert solution.reverse(input) == expected


def test_simple():
    solution = Solution()
    assert solution.reverse(123) == 321
