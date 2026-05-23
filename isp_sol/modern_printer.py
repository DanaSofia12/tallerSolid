"""Impresora moderna: imprime, fax y escaneo (ISP)."""

from .faxable import Faxable
from .printable import Printable
from .scannable import Scannable


class ModernPrinter(Printable, Faxable, Scannable):
    """Implementa solo las interfaces que realmente ofrece."""

    def print(self, document: str) -> None:
        print(f"Printing {document} in color...")

    def fax(self, document: str) -> None:
        print(f"Faxing {document}...")

    def scan(self, document: str) -> None:
        print(f"Scanning {document}...")
