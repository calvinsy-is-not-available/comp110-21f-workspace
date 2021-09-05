"""Repeating a beat in a loop."""

__author__ = "730482431"


reeee: str = input("What beat do you want to repeat? ")
force_of_a_thousand_suns = reeee + " "
i: int = 0
maximum: int = int(input("How many times do you want to repeat it? "))
while i < maximum:
    i = i + 1
    print(force_of_a_thousand_suns * (i - 1) + reeee)
if maximum < 0:
    print("No beat...")