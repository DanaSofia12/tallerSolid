"""Interfaz solo para escaneo (ISP)."""

from abc import ABC, abstractmethod


class Scannable(ABC):
    """Contrato mínimo: escanear un documento."""

    @abstractmethod
    def scan(self, document: str) -> None:
        """Escanea el documento indicado."""
