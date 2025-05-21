import random


class Board:
    def __init__(self, width=9, height=9, mines=10):
        """
        width: ширина поля (кол-во столбцов)
        height: высота поля (кол-во строк)
        mines: число мин
        """
        self.width = width
        self.height = height
        self.mines = mines
        self._generate()

    def _generate(self):
        """Генерация поля: расставляем мины и считаем цифры."""
        self.grid = [['.' for _ in range(self.width)]
                     for _ in range(self.height)]
        self.revealed = [[False] * self.width
                         for _ in range(self.height)]
        self.flagged = [[False] * self.width
                        for _ in range(self.height)]
        all_positions = list(range(self.width * self.height))
        mine_positions = random.sample(all_positions, self.mines)
        for pos in mine_positions:
            r, c = divmod(pos, self.width)
            self.grid[r][c] = '*'
        self.numbers = [[
            self._count_adjacent(r, c) if self.grid[r][c] == '.'
            else '*'
            for c in range(self.width)]
            for r in range(self.height)
        ]

    def _count_adjacent(self, row, col):
        """Возвращает число мин вокруг клетки (row, col)."""
        cnt = 0
        for r in range(max(0, row - 1), min(self.height, row + 2)):
            for c in range(max(0, col - 1), min(self.width, col + 2)):
                if self.grid[r][c] == '*':
                    cnt += 1
        return cnt

    def reveal(self, row, col):
        """
        Открыть клетку (row, col).
        Если это мина — установим game_over=True.
        Если число соседей == 0 — откроем всех соседей рекурсивно.
        """
        if self.flagged[row][col] or self.revealed[row][col]:
            return  # ничего не делаем, если уже открыто или отмечено флажком

        self.revealed[row][col] = True

        if self.grid[row][col] == '*':
            # попали на мину
            self.game_over = True
            return

        # если вокруг нет мин — открываем соседей
        if self.numbers[row][col] == 0:
            for r in range(max(0, row - 1), min(self.height, row + 2)):
                for c in range(max(0, col - 1), min(self.width, col + 2)):
                    if not self.revealed[r][c]:
                        self.reveal(r, c)

    def toggle_flag(self, row, col):
        """
        Поставить или убрать флажок:
        если клетка не открыта, переключаем состояние флага.
        """
        if not self.revealed[row][col]:
            self.flagged[row][col] = not self.flagged[row][col]

    def check_win(self):
        """
        Возвращает True, если все не минные клетки открыты.
        """
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] != '*' and not self.revealed[r][c]:
                    return False
        return True


def count_adjacent_mines(board, row, col):
    """
    Для тестов: считает мины в «сыром» списочном поле.
    board: List[List[str]] с '*' для мин и '.' для пустых.
    """
    count = 0
    height = len(board)
    width = len(board[0]) if height > 0 else 0
    for r in range(max(0, row - 1), min(height, row + 2)):
        for c in range(max(0, col - 1), min(width, col + 2)):
            if (r != row or c != col) and board[r][c] == '*':
                count += 1
    return count
