import sys
import os

def get_resource_path(relative_path):
    """Retorna o caminho absoluto para o recurso (compatível com PyInstaller)."""
    if hasattr(sys, '_MEIPASS'):
        # Quando rodando como executável
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)