"""Paquete LSP refactorizado: subtipos sustituibles sin romper el contrato."""

from .area_calculator import total_area
from .rectangle import Rectangle
from .shape import Shape
from .square import Square

__all__ = ["Rectangle", "Shape", "Square", "total_area"]
