"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"


def test_only_evens_empty_list() -> None:
    """Test for only evens."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_increasing() -> None:
    """Test for only evens."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_irratic() -> None:
    """Test for only evens."""
    xs: list[int] = [2, 5, 4, 100, 27, 28]
    assert only_evens(xs) == [2, 4, 100, 28]


def test_sub_empty_list() -> None:
    """Test for sub."""
    xs: list[int] = []
    ys: int = 0
    z: int = 1
    assert sub(xs, ys, z) == []


def test_sub_increasing() -> None:
    """Test for sub.""" 
    xs: list[int] = [10, 20, 30, 40, 50, 60, 70, 80]
    ys: int = 1
    z: int = 6
    assert sub(xs, ys, z) == [10, 60]


def test_sub_irratic() -> None:
    """Test for sub."""
    xs: list[int] = [20, 50, 10, 60, 2100, 50]
    ys: int = 4
    z: int = 7
    assert sub(xs, ys, z) == [60, 50]


def test_concat_empty() -> None:
    """Test for concat."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_if_one_list_is_empty() -> None:
    """Test for concat."""
    xs: list[int] = []
    ys: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6, 7]


def test_concat_if_both_lists_are_equal() -> None:
    """Test for concat."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [1, 2, 3]
    assert concat(xs, ys) == [1, 2, 3, 1, 2, 3]