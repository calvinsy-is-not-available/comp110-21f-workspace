def head(dish: dict[str, list[str]], san: int) -> dict[str, list[str]]:
    soap: dict[str, list[str]] = {}
    goutoun: list = []
    kagebunshin: list = []
    first_row: list[str] = []
    mtlst: list[str] = []
    for key in dish:
        first_row.append(key)
    i: int = 0
    for column in dish:
        kagebunshin.append(column)
    while i < san:
        goutoun.append(kagebunshin[i])
        i += 1
    print(kagebunshin)
    print(goutoun)
    soap['a'] = [f"{dish['b'][1]}"]
    print(soap)
    i = 0
    while i < san:
        soap[first_row[i]] = [mtlst.append(dish[first_row[i]][i])
        i += 1
    return soap


dishes: dict[str, list[str]] = {'a': ['alpha'], 'b': ['alpha', 'beta', 'theta', 'gamma'], 'c': ['CHOCOLATE'], 'd': ["PICKLE RICK"], 'e': ['DAS IST EIN TRAP'], 'f': ['VERBODEN']}
print(head(dishes, 2))