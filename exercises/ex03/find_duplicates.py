"""Finding duplicate letters in a word."""

__author__ = "123456789"

wordy_bird: str = input("Enter a word: ")
i: int = 0
dup: bool = False

while i < len(wordy_bird):
    char = wordy_bird[i]
    j: int = i + 1
    while j < len(wordy_bird):
        char_1 = wordy_bird[j]
        if char == char_1:
            dup = True
        j = j + 1
    i = i + 1
print("Found duplicate:", dup)