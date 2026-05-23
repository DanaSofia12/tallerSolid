"""Rectángulo con ancho y alto independientes (LSP)."""

from .shape import Shape


class Rectangle(Shape):
    """Rectángulo: ancho y alto pueden ser distintos."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height
