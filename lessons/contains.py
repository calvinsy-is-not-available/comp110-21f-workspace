"""Example of a function that processes a list."""


# We are trying to define a function called 'contains'
# We can give two arguements: a needle that we're trying to search for in a haystack list
#def contains(needle: str, haystack: list[str]) -> bool:
# """Return True if needle is found in haystack, False Otherwise."""
# Return True if needle is found in the haystack, false otherwise
    # Loop through each index in a list 
    # i: int = 0
    #  while i < len(haystack):
        #  if haystack[i] == needle:
            # test if each item stored ast index is equal to the needle 
            # Return True if so
            #    return True
        #   i  += 1
    # Return false after each item
    #   return False

# duplicates found in the haystack will not return true twice. If needle == haystack: True will return and the programe will terminate


def main() -> None:
    "A Main function."
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kris", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in haystack, False Otherwise."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
                return True
        i  += 1
    return False