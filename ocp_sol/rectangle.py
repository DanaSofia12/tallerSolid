"""Rectángulo como figura extensible (OCP)."""

from .shape import Shape


class Rectangle(Shape):
    """Rectángulo definido por ancho y alto."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height
