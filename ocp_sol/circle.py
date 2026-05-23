"""Círculo como figura extensible (OCP)."""

from math import pi

from .shape import Shape


class Circle(Shape):
    """Círculo definido por su radio."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return pi * self.radius**2
