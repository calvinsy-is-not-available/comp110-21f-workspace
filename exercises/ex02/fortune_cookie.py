"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730482431"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says... ")
key: int 
key = randint(1, 4)
if key == 2: 
    print("Peace will guide your heart to a life where the sequence of your dreams will know no bounds to joy.")
else:
    if key == 3:
        print("You shall see the world through roses and feel life through endless waves of love.")
    if key == 1:
        print("Following a dream, New Years' light will bless you every morning.")
    if key == 4:
        print("You will change the world through your conviction of kindness and camaraderie.")
print("Now, go spread positive vibes!")
