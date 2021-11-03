"""An exercise in remainders and boolean logic."""

__author__ = "730482431"


one: int = int(input("Enter an int: "))

if one % 2 == 0 and one % 7 == 0:
    print("TAR HEELS")
else:
    if one % 2 == 0:
        print("TAR")
    else:
        if one % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")
