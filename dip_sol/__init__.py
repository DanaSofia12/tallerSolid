"""Paquete DIP refactorizado: depender de abstracciones, no de detalles."""

from .data_source import DataSource
from .database import BackEnd
from .front_end import FrontEnd

__all__ = ["BackEnd", "DataSource", "FrontEnd"]
