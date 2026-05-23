"""Contrato base para figuras geométricas (OCP)."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Figura cerrada para extensión sin modificar código existente."""

    @abstractmethod
    def calculate_area(self) -> float:
        """Calcula y devuelve el área de la figura."""
