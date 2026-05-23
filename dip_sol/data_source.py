"""Abstracción de acceso a datos (DIP)."""

from abc import ABC, abstractmethod


class DataSource(ABC):
    """Contrato que el front-end consume; no depende de implementaciones concretas."""

    @abstractmethod
    def get_data_from_database(self) -> str:
        """Obtiene datos desde la fuente configurada."""
