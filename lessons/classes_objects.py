"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str 
    toppings: int 
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings

    def price(self, tax) -> float:
        """Calculate the price of a Pizza."""
        total: float = 0.0
        # TODO -- compute price
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        total += self.toppings * tax
        if self.extra_cheese:
            total += 1
        total *= tax
        return total


# How can we set up a Pizza:
a_pizza: Pizza = Pizza("large", 3)
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")


another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")