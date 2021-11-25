"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730482431"


class Simpy:
    """A Simp for numpy."""
    values: list[float]

    def __init__(self, values: list[float]): 
        """Initialization of Simpy."""
        self.values = values

    def __str__(self) -> str:
        """Automagically converts values to a str."""
        return f"Simpy({str(self.values)})"

    def fill(self, y: float, x: int) -> None: 
        """Fills in the values like range."""
        self.values = []
        result = self.values
        i = 0
        while i < x:
            result.append(y)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in values like range, but increments by a state step."""
        if step == 0.0:
            step = 1.0
        self.values = []
        result = self.values
        result.append(start)
        i = 0
        threshold: float = stop / step
        if abs(step) < 1.0:
            rep: int = (int(threshold - 1))
        else: 
            rep: int = (int(threshold - 2))
        while i < rep:
            num: float = result[i] + step
            result.append(num)
            i += 1 
    
    def sum(self) -> float:
        """Sums the elms in a list of floats."""
        i: int = 0
        total: float = 0.0
        while i < len(self.values):
            total += self.values[i]
            i += 1
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Sum operator overload for simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
            return result
        else:
            i = 0 
            while i < len(self.values):
                result.values.append(self.values[i] + rhs)
                i += 1
            return result 

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponential operator overload for simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
            return result
        else:
            i = 0 
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs)
                i += 1
            return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Equality operator overlaod for Simpy."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
            return result
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs)
                i += 1
            return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than operator overload for Simpy."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
            return result
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs)
                i += 1
            return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription operator overload for Simpy."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            i: int = 0
            result = Simpy([])
            while i < len(rhs):
                if rhs[i]:
                    result.values.append(self.values[i])
                else:
                    pass
                i += 1
            return result