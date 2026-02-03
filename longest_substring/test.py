import pytest

from longest_substring.solution import Solution


@pytest.mark.parametrize("s, expected_len", [
    ["", 0],
    [" ", 1],
    ["  ", 1],
    ["a", 1],
    ["abcabcbb", 3],
    ["bbbbb", 1],
    ["pwwkew", 3],
    ["dvdf", 3],
    ["anviaj", 5],
    ["tmmzuxt", 5],
    ["abcdefghijklmnopqrstuvwxyz", 26],
])
def test_calc_length_longest_substring(s: str, expected_len: int):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(s) == expected_len