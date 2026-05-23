"""Paquete ISP refactorizado: interfaces segregadas por capacidad."""

from .faxable import Faxable
from .modern_printer import ModernPrinter
from .old_printer import OldPrinter
from .printable import Printable
from .scannable import Scannable

__all__ = [
    "Faxable",
    "ModernPrinter",
    "OldPrinter",
    "Printable",
    "Scannable",
]
