"""List utility functions part 2."""

__author__ = "123456789"

# Define your functions below


def all_evens(x: list[int]) -> list[int]:
    """Returns list (if applicable) of even ints."""
    i: int = 0
    xs: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            xs.append(x[i])
        i += 1
    return xs


def sub(x: list[int], y: int, z: int) -> list[int]:
    """Creates the subset of an Index"""
    xs: list[int] = []
    zs: int = len(x) - 1
    if not y > 0:
        y = 1
    if not z < zs:
        z = len(x)
    if xs == []:
        return []
    if y > len(x):
        return []
    if z < 0:
        return []
    xs = [x[y - 1], x[z - 1]]
    return xs


print(all_evens([4, 4, 4]))