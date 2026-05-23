"""Contrato común para figuras sustituibles (LSP)."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Tipo base: las subclases deben poder usarse donde se espera Shape."""

    @abstractmethod
    def calculate_area(self) -> float:
        """Calcula y devuelve el área de la figura."""
