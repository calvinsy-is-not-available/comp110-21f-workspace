"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
deins_nummer: int = int(input("Depth: "))
i: int = 0
while i < deins_nummer:
    print(TREE + TREE * (i))
    i = i + 1
