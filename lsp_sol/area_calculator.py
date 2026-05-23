"""Cálculo de área sobre cualquier Shape sustituible (LSP)."""

from .shape import Shape


def total_area(shapes: list[Shape]) -> float:
    """Suma áreas aceptando cualquier subtipo de Shape sin comportamiento inesperado."""
    return sum(shape.calculate_area() for shape in shapes)
