def head(dish: dict[str, list[str]], san: int) -> dict[str, list[str]]:
    soap: dict[str, list[str]] = {}
    i: int = 0
    first_row: list[str] = []
    for key in dish:
        first_row.append(key)
    for column in dish:
        kagebunshin: list[str] = []
        while i < san:
            kagebunshin.append(column)
            i += 1
    print(kagebunshin)
    return soap


dishes: dict[str, list[str]] = {'a': ['alpha'], 'b': ['alpha', 'beta'], 'c': ['CHOCOLATE'], 'd': ["PICKLE RICK"], 'e': ['DAS IST EIN TRAP'], 'f': ['VERBODEN']}
print(head(dishes, 2))