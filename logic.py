class Board:
    def __init__(self, width=10, height=10, mines=20):
        # TODO: реалізувати генерацію поля
        pass


def count_adjacent_mines(board, row, col):
    """
    Підраховує кількість мін навколо клітини (row, col).
    :param board: матриця, де '*' = міна, '.' = порожня клітинка
    """
    count = 0
    for i in range(max(0, row - 1), min(len(board), row + 2)):
        for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
            if (i != row or j != col) and board[i][j] == '*':
                count += 1
    return count
