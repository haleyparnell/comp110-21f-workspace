"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730514769"


def test_only_evens_1() -> None:
    """Empty list."""
    assert only_evens([]) == []


def test_only_evens_2() -> None:
    """Negative and even."""
    assert only_evens([-1, -2, 3, -4]) == [-2, -4]


def test_only_evens_3() -> None:
    """Another test."""
    assert only_evens([1, 2, 3, 4, 4, 2, 6]) == [2, 4, 4, 2, 6]


def test_sub_1() -> None:
    """Test."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_2() -> None:
    """Test."""
    a_list = [-2, 20, 16, 40]
    assert sub(a_list, 2, 3) == [16, 40]


def test_sub_3() -> None:
    """Test."""
    a_list = [-1, -2, 45, 40, 54, 32]
    assert sub(a_list, 1, 4) == [-2, 45, 40, 54, 32]


def test_concat_1() -> None:
    """Test."""
    first_list = [10, 20, 30, 40]
    second_list = [10, 20, 30, 40]
    assert concat(first_list, second_list) == [10, 20, 30, 40, 10, 20, 30, 40]


def test_concat_2() -> None:
    """Test."""
    first_list = [1, 3, -1, 2]
    second_list = [6, 6, 9, 0]
    assert concat(first_list, second_list) == [1, 3, -1, 2, 6, 6, 9, 0]


def test_concat_3() -> None:
    """Test."""
    first_list = [11, 20, 90, 40, 54]
    second_list = [12, 2, 30]
    assert concat(first_list, second_list) == [11, 20, 90, 40, 54, 12, 2, 30]