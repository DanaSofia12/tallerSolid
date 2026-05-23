"""Impresora antigua: solo imprime, sin fax ni escaneo (ISP)."""

from .printable import Printable


class OldPrinter(Printable):
    """Implementa únicamente Printable; no depende de fax ni scan."""

    def print(self, document: str) -> None:
        print(f"Printing {document} in black and white...")
