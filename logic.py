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
