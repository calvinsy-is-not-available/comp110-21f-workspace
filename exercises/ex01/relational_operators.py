"""Exercise 01 For Comp 110 fall 2021: Rational Operators Assignment."""

__author__ = "730482431"

x: str = input("Left-Hand_side: ")
y: str = input("Right-Hand_side: ")
x1: int = int(x)
y1: int = int(y)
print(x, "< " + y, " is", x1<y1)
print(x, ">= " + y, " is", x1>=y1)
print(x, "== " + y, " is", x1==y1)
print(x, "!= " + y, " is", x1!=y1)