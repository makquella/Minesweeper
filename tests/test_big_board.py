import pytest
from logic import Board


@pytest.mark.slow
def test_big_board_generation():
    """Генерація поля 30×16 із 99 мінами до 0,2 с."""
    b = Board(width=30, height=16, mines=99)
    assert sum(cell == '*' for row in b.grid for cell in row) == 99
