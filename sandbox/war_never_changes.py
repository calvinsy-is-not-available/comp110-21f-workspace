def favorite_colors(x: dict[str, str]) -> list[str]:
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
    for color in listy_2:
        listy_2.strip('""')

    i = 0
    while i < len(listy_2):
        if listy_2[i] in 

    
        
my_dict: dict[str, str] = {"calvin": "purple", "tay": "red", "dad": "blue", "jim": "purple"}
lst = list(my_dict.values()) 
print(lst)