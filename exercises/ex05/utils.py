"""List utility functions part 2."""

__author__ = "123456789"


def only_evens(x: list[int]) -> list[int]:
    """Returns list (if applicable) of even ints."""
    if x == []:
        return []
    i: int = 0
    xs: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            xs.append(x[i])
        i += 1
    return xs


def sub(x: list[int], y: int, z: int) -> list[int]:
    """Creates the subset of an Index."""
    zs: int = len(x)
    if len(x) == 0:
        return []
    if y == z:
        return []
    if y < 0:
        y = 0
    if z > zs:
        z = zs
    if y == zs or y > zs:
        return []
    if z == 0:
        return []
    if z < 0:
        return []
    xs = [x[y], x[z - 1]]
    return xs


def concat(x: list[int], y: list[int]) -> list[int]:
    """Ties to Strings Together."""
    if x == [] and y == []:
        return []
    i: int = 0
    while i < len(y):
        x.append(y[i])
        i += 1
    return x