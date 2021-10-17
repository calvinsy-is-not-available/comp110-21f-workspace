"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730482431"


def test_invert_of_two_equivalent_values() -> None:
    """Test for invert."""
    my_dict: dict[str, str] = {"one": "purple", "two": "purple"}
    assert invert(my_dict) == KeyError("key given is not unique.")


def test_invert_of_a_short_string() -> None:
    """Test for invert."""
    my_dict: dict[str, str] = {"kevin": "calvin", "jaden": "larry", "pernell": "eugene"}
    assert invert(my_dict) == {"calvin": "kevin", "larry": "jaden", "eugene": "pernell"}


def test_invert_of_a_long_string() -> None:
    """Test for invert."""
    my_dict: dict[str, str] = {"kevvvvvvvvvviiiiiiiiiiiiinnnnnnnnn": "calvin"}
    assert invert(my_dict) == {"calvin": "kevvvvvvvvvviiiiiiiiiiiiinnnnnnnnn"}


def test_favorite_color_two_favorite_colors() -> None:
    """Test for fav colors."""
    my_dict: dict[str, str] = {"calvin": "purple", "tay": "purple", "dad": "blue", "jim": "purple", "mom": "blue", "uncle": "blue", "timmy": "green", "rick": "yellow", "morty": "yellow"}
    assert favorite_color(my_dict) == "purple"


def test_favorite_color_an_increasing_count() -> None:
    """Test for fav colors."""
    my_dict: dict[str, str] = {"kaki": "purple", "Prof KJ": "red", "Marc": "red", "UTAs": "green", "mom": "green", "dad": "green"}
    assert favorite_color(my_dict) == "green"


def test_favorite_color_a_decreasing_count() -> None:
    """Test for fav colors."""
    my_dict: dict[str, str] = {"kaki": "green", "Prof KJ": "green", "Marc": "green", "UTAs": "red", "mom": "red", "dad": "purple"}
    assert favorite_color(my_dict) == "green"


def test_count_empty_listy() -> None:
    """Test for count."""
    lsty: list[str] = []
    assert count(lsty) == {}


def test_count_increasing_numbers() -> None:
    """Test for count."""
    lsty: list[str] = ["yellow", "blue", "blue", "green", "green", "green"]
    assert count(lsty) == {"yellow": 1, "blue": 2, "green": 3}


def test_count_decresing_numbers() -> None:
    """Test for count."""
    lsty: list[str] = ["green", "green", "green", "blue", "blue", "yellow"]
    assert count(lsty) == {"yellow": 1, "blue": 2, "green": 3}