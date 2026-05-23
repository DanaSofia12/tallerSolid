"""Implementación concreta de acceso a base de datos (DIP)."""

from .data_source import DataSource


class BackEnd(DataSource):
    """Detalle de bajo nivel: depende de la abstracción DataSource."""

    def get_data_from_database(self) -> str:
        return "Data from the database"
