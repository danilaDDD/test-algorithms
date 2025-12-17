from typing import Callable, Any

import pytest

from sort.sort import bubble_sort, insertion_sort, cocktail_sort, selection_sort


class Number:
    def __init__(self, value: int):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f"Number({self.value})"


@pytest.fixture(scope="module")
def sort() -> Callable[[list[Number], bool], list[Number]]:
    return cocktail_sort


def get_test_cases(sort):
    return [
        ([], [], [], sort),
        ([1], [1], [1], sort),
        ([2, 1], [2, 1], [1, 2], sort),
        ([1, 2, 3], [3, 2, 1], [1, 2, 3], sort),
        ([3, 2, 1], [3, 2, 1], [1, 2, 3], sort),
        ([5, 1, 4, 2, 8], [8, 5, 4, 2, 1], [1, 2, 4, 5, 8], sort),
    ]


class TestSort:
    def __assert_sequence(self, *expected_numbers, actual_numbers: list[Number]):
        expected = [Number(num) for num in expected_numbers]
        assert actual_numbers == expected

    @pytest.mark.parametrize(
        "input, expected, reverse_expected, sort",
        get_test_cases(bubble_sort) +
        get_test_cases(insertion_sort) +
        get_test_cases(cocktail_sort) +
        get_test_cases(selection_sort)
    )
    def test_sort(self, input, expected, reverse_expected, sort):
        input_numbers = [Number(num) for num in input]

        reverse_sorted_numbers = sort(input_numbers, reverse=True)
        self.__assert_sequence(*expected, actual_numbers=reverse_sorted_numbers)

        sorted_numbers = sort(input_numbers, reverse=False)
        self.__assert_sequence(*reverse_expected, actual_numbers=sorted_numbers)