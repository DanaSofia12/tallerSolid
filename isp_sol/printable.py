"""Interfaz solo para impresión (ISP)."""

from abc import ABC, abstractmethod


class Printable(ABC):
    """Contrato mínimo: imprimir un documento."""

    @abstractmethod
    def print(self, document: str) -> None:
        """Imprime el documento indicado."""
