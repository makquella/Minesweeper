import os, sys
import pytest
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, ROOT)        # ← додає корінь репозиторію в sys.path
from logic import Board


@pytest.fixture
def empty_3x3():
    """Поле 3×3 без мін – для flood-fill-перевірок."""
    b = Board(width=3, height=3, mines=0)
    return b


@pytest.fixture
def board_5x5():
    """Поле 5×5 із 5 мінами – генерується випадково."""
    return Board(width=5, height=5, mines=5)
