"""Practice with dictionaries."""

__author__ = "123456789"

# Define your functions below
def inverse(x: dict[str, str]) -> dict[str, str]:
    """Gives the inverse of a given dict."""
    i: int = 0
    listy: list[str] = []
    listy_2: list[str] = []
    for key in x:
        listy.append(key)
    while i < len(listy):
        listy_2.append(x[f"{listy[i]}"])
        i += 1
    print(listy)
    print(listy_2)
    i = 0
    x_inverse: dict[str, str] = {}
    while i < len(listy) and i < len(listy_2):
        x_inverse[f"{listy_2[i]}"] = f"{listy[i]}"
        i += 1
    i = 0
    while i < len(listy_2):
        b: int = i + 1
        while b < len(listy_2):
            if listy_2[b] == listy_2[i]:
                raise KeyError("key given is not unique.")
            b += 1 
        i += 1
    return x_inverse
