import logic


def test_generate_mines_count():
    # Берём поле 5×4 и 7 мин
    b = logic.Board(width=5, height=4, mines=7)
    # Считаем звёздочки в grid
    flat = sum(cell == '*' for row in b.grid for cell in row)
    assert flat == 7


def test_count_adjacent_mines():
    board = [
        ['*', '.', '.'],
        ['.', '.', '*'],
        ['.', '*', '.'],
    ]
    count = logic.count_adjacent_mines(board, 1, 1)
    assert count == 3


def test_reveal_flood_fill():
    # Поле 3×3 без мин — при reveal(1,1) откроются все клетки
    b = logic.Board(width=3, height=3, mines=0)
    b.reveal(1, 1)
    assert all(b.revealed[r][c] for r in range(3) for c in range(3))


def test_reveal_mine_sets_game_over():
    # Поле 2×2 с одной миной в (0,0)
    b = logic.Board(width=2, height=2, mines=1)
    # Найдём координаты мины
    coords = [(r, c) for r in range(2) for c in range(2) if b.grid[r][c] == '*'][0]
    b.reveal(*coords)
    assert getattr(b, 'game_over', False) is True


def test_toggle_flag():
    b = logic.Board(width=2, height=2, mines=1)
    b.toggle_flag(0, 0)
    assert b.flagged[0][0] is True
    b.toggle_flag(0, 0)
    assert b.flagged[0][0] is False


def test_check_win():
    # Поле 2×2 с одной миной
    b = logic.Board(width=2, height=2, mines=1)
    # Открываем все безопасные клетки
    for r in range(2):
        for c in range(2):
            if b.grid[r][c] != '*':
                b.reveal(r, c)
    assert b.check_win() is True
