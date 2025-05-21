import logic

def test_count_adjacent_mines():
    board = [
        ['*', '.', '.'],
        ['.', '.', '*'],
        ['.', '*', '.']
    ]
    count = logic.count_adjacent_mines(board, 1, 1)
    assert count == 3
