from unittest.mock import patch
from logic import Board


def test_generate_exact_positions():
    positions = [0, 6, 8]        # клітини 0,6,8 мають стати мінами
    with patch("random.sample", return_value=positions):
        b = Board(width=3, height=3, mines=3)
    mines = [(r, c) for r in range(3) for c in range(3) if b.grid[r][c] == '*']
    assert mines == [(0, 0), (2, 0), (2, 2)]  # divmod(0/3/8)
