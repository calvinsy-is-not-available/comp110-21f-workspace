"""Practice with dictionaries."""

__author__ = "730482431"

# Define your functions below


def invert(x: dict[str, str]) -> dict[str, str]:
    """Gives the inverse of a given dict."""
    i: int = 0
    listy: list[str] = []
    listy_2: list[str] = []
    for key in x:
        listy.append(key)
    while i < len(listy):
        listy_2.append(x[f"{listy[i]}"])
        i += 1
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


def favorite_color(x: dict[str, str]) -> str:
    """Gives consenus of a favorite color from a dict."""
    i: int = 0
    listy: list[str] = []
    listy_2: list[str] = []
    favorite_color: str = ""
    for key in x:
        listy.append(key)
    while i < len(listy):
        listy_2.append(x[f"{listy[i]}"])
        i += 1
    dish: dict[str, int] = {}
    for item in listy_2:
        if item not in dish:
            dish[item] = 1
        else:
            if item in dish:
                dish[item] += 1
    listy_3: list[str] = []
    listy_4: list[int] = []
    for key in dish:
        listy_3.append(key)
    i = 0
    while i < len(listy_3):
        listy_4.append(dish[listy_3[i]])
        i += 1
    dish_inverse: dict[int, str] = {}
    i = 0
    while i < len(listy_4):
        b: int = i + 1
        while b < len(listy_4):
            if listy_4[b] == listy_4[i]:
                listy_4.pop(b)
            b += 1
        i += 1
    i = 0
    while i < len(listy_3) and i < len(listy_4):
        dish_inverse[listy_4[i]] = f"{listy_3[i]}"
        i += 1
    m_a_x: int = max(listy_4)
    favorite_color = f"{dish_inverse[m_a_x]}"
    return favorite_color


def count(x: list[str]) -> dict[str, int]:
    """Tells you the count in a list."""
    dish: dict[str, int] = {}
    if x == []:
        return {}
    for item in x:
        if item not in dish:
            dish[item] = 1
        else:
            if item in dish:
                dish[item] += 1
    return dish