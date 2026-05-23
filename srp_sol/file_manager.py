"""Lectura y escritura de archivos en disco (SRP)."""

from pathlib import Path


class FileManager:
    """Gestiona operaciones de lectura y escritura sobre un archivo."""

    def __init__(self, filename: str) -> None:
        self.path = Path(filename)

    def read(self, encoding: str = "utf-8") -> str:
        """Lee y devuelve el contenido del archivo como texto."""
        return self.path.read_text(encoding=encoding)

    def write(self, data: str, encoding: str = "utf-8") -> None:
        """Escribe el texto indicado en el archivo."""
        self.path.write_text(data, encoding=encoding)
