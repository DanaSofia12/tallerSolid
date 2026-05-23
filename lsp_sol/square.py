"""Cuadrado como figura propia, no como subtipo de Rectangle (LSP)."""

from .shape import Shape


class Square(Shape):
    """Cuadrado: un solo lado; no hereda de Rectangle para no romper su contrato."""

    def __init__(self, side: float) -> None:
        self.side = side

    def calculate_area(self) -> float:
        return self.side**2
