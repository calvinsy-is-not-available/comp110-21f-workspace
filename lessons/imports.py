"""Examples of imoprting functions."""

from lessons import helpers


from lessons import helpers as hp
# Import using an alias

# Import names directly from the globals of a module
from lessons.helpers import THE_ANSWER, powerful


def main() -> None:
    # acesses the first import
    print(helpers.powerful(2, 4))
    # acesses the alias import
    print(hp.THE_ANSWER)
    # call the imported function directly
    print(powerful(2, 10))
    print(THE_ANSWER)
    print(f"imports.py: {__name__}")


if __name__ == "__main__":
    main()
    