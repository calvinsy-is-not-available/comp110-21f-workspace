"""Counting letters in a string."""

__author__ = "730482431"


your_letter: str = input("what is your letter?: ")
your_word: str = input("what is your word: ")
counter: int = 0 
maximum = int(your_letter in your_word)
while counter <= maximum:
    counter = counter + 1
    if maximum == 0:
        print("Count: 0")
    else:
        if counter > maximum:
            print("Count:", + counter)