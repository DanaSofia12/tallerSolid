"""Capa de presentación que depende de la abstracción (DIP)."""

from .data_source import DataSource


class FrontEnd:
    """Alto nivel: recibe cualquier DataSource, no una clase concreta BackEnd."""

    def __init__(self, back_end: DataSource) -> None:
        self.back_end = back_end

    def display_data(self) -> None:
        data = self.back_end.get_data_from_database()
        print("Display data:", data)
