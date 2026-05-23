"""Compresión y descompresión ZIP de archivos (SRP)."""

from pathlib import Path
from zipfile import ZipFile


class FileCompressor:
    """Gestiona compresión y descompresión de un archivo en formato ZIP."""

    def __init__(self, filename: str) -> None:
        self.path = Path(filename)

    def compress(self) -> None:
        """Comprime el archivo en un archivo .zip con el mismo nombre base."""
        zip_path = self.path.with_suffix(".zip")
        with ZipFile(zip_path, mode="w") as archive:
            archive.write(self.path, arcname=self.path.name)

    def decompress(self, extract_to: str = ".") -> None:
        """Extrae el contenido del .zip asociado al directorio indicado."""
        zip_path = self.path.with_suffix(".zip")
        with ZipFile(zip_path, mode="r") as archive:
            archive.extractall(path=extract_to)
