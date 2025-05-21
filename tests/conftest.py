import os
import sys
import pytest

# Додаємо корінь репозиторію в sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, ROOT)

from logic import Board  # noqa: E402


@pytest.fixture
def empty_3x3():
    """Поле 3×3 без мін – для flood-fill-перевірок."""
    return Board(width=3, height=3, mines=0)


@pytest.fixture
def board_5x5():
    """Поле 5×5 із 5 мінами – генерується випадково."""
    return Board(width=5, height=5, mines=5)
