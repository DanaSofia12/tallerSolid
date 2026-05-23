"""Interfaz solo para envío por fax (ISP)."""

from abc import ABC, abstractmethod


class Faxable(ABC):
    """Contrato mínimo: enviar un documento por fax."""

    @abstractmethod
    def fax(self, document: str) -> None:
        """Envía el documento por fax."""
