"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730514769"


def test_only_evens_1() -> None:
    assert only_evens([]) == []


def test_only_evens_2() -> None:
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_3() -> None:
    assert only_evens([1, 2, 3, 4, 4, 2, 6]) == [2, 4, 4, 2, 6]