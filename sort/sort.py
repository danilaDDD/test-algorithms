from collections import deque
from typing import Any, List

def if_swap(a, b, reverse):
    return a < b if reverse else a > b


def bubble_sort(items: List[Any], reverse=False) -> List[Any]:
    new_items = items.copy()
    n = len(new_items)
    for i in range(n):
        for j in range(1, n - i):
            if if_swap(new_items[j - 1], new_items[j], reverse):
                new_items[j], new_items[j - 1] = new_items[j - 1], new_items[j]

    return new_items


def insertion_sort(items: List[Any], reverse=False) -> List[Any]:
    new_items = items.copy()
    n = len(new_items)
    for i in range(n - 1):
        j = i + 1
        key = new_items[j]
        while j > 0 and (new_items[j - 1] < key if reverse else new_items[j - 1] > key):
            new_items[j], new_items[j - 1] = new_items[j - 1], new_items[j]
            j -= 1

    return new_items


def cocktail_sort(items: List[Any], reverse=False) -> List[Any]:
    new_items = items.copy()
    n = len(new_items)

    if len(new_items) < 2:
        return new_items

    for i in range(n):
        right = new_items[n - i - 1]
        swapped_index = None
        for j in range(i, n - i):
            if if_swap(new_items[j], right, reverse):
                right = new_items[j]
                swapped_index= j
        if swapped_index is not None:
            new_items[n - i - 1], new_items[swapped_index] = new_items[swapped_index], new_items[n - i - 1]

        left = new_items[i]
        swapped_index = None
        for j in range(n - i - 2, i, -1):
            if if_swap(left, new_items[j], reverse):
                left = new_items[j]
                swapped_index = j

        if swapped_index is not None:
            new_items[i], new_items[swapped_index] = new_items[swapped_index], new_items[i]

    return new_items


def selection_sort(items: List[Any], reverse=False) -> List[Any]:
    n = len(items)
    new_items = items.copy()
    for start in range(n):
        selected, index = select_item(start, new_items, reverse)
        if index != start:
            new_items[start], new_items[index] = new_items[index], new_items[start]

    return new_items

def select_item(start: int, items: List[Any], reverse=False) -> Any:
    select = items[start]
    select_index = start
    for i in range(start + 1, len(items)):
        if if_swap(select, items[i], reverse):
            select = items[i]
            select_index = i

    return select, select_index
