"""Instructions of programs implemented elsewhere."""


THE_ANSWER: int = 42


def powerful(x: float, n: float) -> float:
    """returns x raided to the power of n."""
    x = x ** n 
    return x


if __name__ == "__main__":
    # Python idiom to call main
    print(f"helpers.py: {__name__}")
    print("Evaluated as a program")
else:
    # Typically not common to do ANYTHING with the case where a module is imported
    print("Evaluated as an imported module")