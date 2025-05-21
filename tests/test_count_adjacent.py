import pytest
from logic import count_adjacent_mines

CASES = [
    # board, (row, col), expected
    (
        [
            ['*', '.', '.'],
            ['.', '.', '*'],
            ['.', '*', '.'],
        ],
        (1, 1),
        3,
    ),
    (
        [
            ['*', '*', '*'],
            ['*', '.', '*'],
            ['*', '*', '*'],
        ],
        (1, 1),
        8,
    ),
]


@pytest.mark.parametrize("board, coord, expected", CASES)
def test_adjacent(board, coord, expected):
    row, col = coord
    assert count_adjacent_mines(board, row, col) == expected
