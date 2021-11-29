"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730514769"


def test_invert_1() -> None:
    """Simple test."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert_2() -> None:
    """Simple test."""
    assert invert({'Haley': 'Michelle', 'John': 'Haley'}) == {'Michelle': 'Haley', 'Haley': 'John'}


def test_invert_3() -> None:
    """Simple test."""
    assert invert({'comp110': 'soul-crushing'}) == {'soul-crushing': 'comp110'}


def test_favorite_color_1() -> None:
    """Simple test."""
    assert favorite_color({'Haley': 'blue', 'Michelle': 'purple', 'John': 'blue'}) == 'blue'


def test_favorite_color_2() -> None:
    """Simple test."""
    assert favorite_color({'Haley': 'pink', 'Michelle': 'purple', 'John': 'pink', 'Kris': 'purple', 'Kaki': 'purple'}) == 'purple'


def test_favorite_color_3() -> None:
    """Simple test."""
    assert favorite_color({'Haley': 'black', 'Michelle': 'black', 'John': 'black'}) == 'black'


def test_count_1() -> None:
    """Simple test."""
    assert count(['a', 'a', 'a', 'b', 'c', 'a']) == {'a': 4, 'b': 1, 'c': 1}


def test_count_2() -> None:
    """Simple test."""
    assert count(['blue', 'green', 'green', 'green', 'blue', 'blue']) == {'blue': 3, 'green': 3}


def test_count_3() -> None:
    """Simple test."""
    assert count(['UNC', 'UNC', 'DUKE', 'NCSU', 'UNC', 'DUKE']) == {'UNC': 3, 'DUKE': 2, 'NCSU': 1}