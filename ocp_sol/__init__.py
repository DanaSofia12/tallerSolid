"""Paquete OCP refactorizado: abierto a extensión, cerrado a modificación."""

from .circle import Circle
from .rectangle import Rectangle
from .shape import Shape

__all__ = ["Circle", "Rectangle", "Shape"]
