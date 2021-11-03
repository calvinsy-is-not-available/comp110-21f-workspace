def head(dish: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    soap: dict[str, list[str]] = {}
    kagebunshin: list[str] = []
    tensei: list[str] = []
    for shadow_clones in dish:
        kagebunshin.append(shadow_clones)
    i: int = 0
    print(kagebunshin)
    print(dish[kagebunshin[0]][0])
    while i < len(kagebunshin):
        tensei.append(dish[kagebunshin[i]][i])
        i += 1
    print(tensei)
    i = 0
    return soap



dishes: dict[str, list[str]] = {'a': ['alpha'], 'b': ['alpha', 'beta', 'theta', 'gamma'], 'c': ['CHOCOLATE'], 'd': ["PICKLE RICK"], 'e': ['DAS IST EIN TRAP'], 'f': ['VERBODEN']}
print(head(dishes, 2))