def head(dish: dict[str, list[str]], san: int) -> dict[str, list[str]]:
    soap: dict[str, list[str]] = {}
    goutoun: list = []
    kagebunshin: list = []
    i: int = 0
    for column in dish:
        kagebunshin.append(column)
    while i < san:
        goutoun.append(kagebunshin[i])
        i += 1
    print(kagebunshin)
    print(goutoun)
    for items in goutoun:
        soap[items] = dish[items]
    return soap


dishes: dict[str, list[str]] = {'a': ['alpha'], 'b': ['alpha', 'beta'], 'c': ['CHOCOLATE'], 'd': ["PICKLE RICK"], 'e': ['DAS IST EIN TRAP'], 'f': ['VERBODEN']}
print(head(dishes, 2))