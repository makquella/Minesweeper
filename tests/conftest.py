import pytest
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
