"""Exercise 01 For Comp 110 fall 2021: Numeric Operators Assignment."""

__author__ = "730482431"

der_nummer_str: str = input("Left-Hand_side: ")
der_nummer_str_zwei: str = input("Right-Hand_side: ")
der_nummer_int: int = int(der_nummer_str)
der_nummer_int_zwei: int = int(der_nummer_str_zwei)
print(der_nummer_str, "** " + der_nummer_str_zwei, " is", der_nummer_int ** der_nummer_int_zwei)
print(der_nummer_str, "/ " + der_nummer_str_zwei, " is", der_nummer_int / der_nummer_int_zwei)
print(der_nummer_str, "// " + der_nummer_str_zwei, " is", der_nummer_int // der_nummer_int_zwei)
print(der_nummer_str, "% " + der_nummer_str_zwei, " is", der_nummer_int % der_nummer_int_zwei)