"""List utility functions."""

__author__ = "730482431"


a: bool
b: bool


def all(x: list[int], y: int) -> bool:
    """Returns a bool: True if all ints are the same."""
    i: int = 0
    global a
    while i < len(x):
        if x[i] == y:
            a = True
        else:
            a = False
            return a
        i += 1
    return a


def is_equal(x: list[int], y: list[int]) -> bool:
    """Determines if the indicies of two lists are equivalent."""
    global b
    if x == [] and y == []:
        return True
    if x == []:
        return False
    i: int = 0
    while i < len(x):
        if x[i] == y[i]:
            b = True
        if x[i] == y[i]:
            if len(y) != len(x):
                return False
        elif y == []:
            b = False
            return b
        else:
            b = False
            return b
        i += 1
    return b


def max(x: list[int]) -> int:
    """Returns the greatest value from a list of ints."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    m_a_x: int = 0
    num: int = x[0]
    while i < len(x):
        j: int = i - 1
        num_2: int = x[j]
        if x[0] < num:
            m_a_x = num
        else:
            if x[0] > num or x[0] == num:
                m_a_x = x[0]
            elif num_2 > num:
                m_a_x = num_2
            m_a_x = x[0]
        i += 1
        num = x[0 + i - 1]
    return m_a_x