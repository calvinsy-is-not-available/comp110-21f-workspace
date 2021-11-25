"""Example of optional parameters and union type parameters."""

from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """Prints a delightful welcome message."""
    result: str = "Hello, "
    if isinstance(name, str):
        return result + name
    elif isinstance(name, float):
        return result + "alien from sector " + str(name)
    else:
        return result + "COMP" + str(name)


# Calling hello with no arguments leads to the default value(s)
print(hello())
# Calling hello with one argument overrides the default value(s)
print(hello(110))
print(hello(3.14))