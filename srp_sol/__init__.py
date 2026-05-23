"""Paquete SRP refactorizado: una responsabilidad por clase."""

from .file_compressor import FileCompressor
from .file_manager import FileManager

__all__ = ["FileCompressor", "FileManager"]
