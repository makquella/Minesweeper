import pygame

CELL_SIZE = 32
COLORS = {
    'covered': (192, 192, 192),
    'revealed': (224, 224, 224),
    'flag': (255, 0, 0),
    'mine': (0, 0, 0),
    'text': (0, 0, 255),
    'border': (0, 0, 0),
}


class GameUI:
    def __init__(self, board, width=None, height=None):
        pygame.init()
        win_w = width or board.width * CELL_SIZE
        win_h = height or board.height * CELL_SIZE
        self.screen = pygame.display.set_mode((win_w, win_h))
        pygame.display.set_caption("Minesweeper")
        self.font = pygame.font.SysFont(None, CELL_SIZE // 2)
        self.board = board

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Левая и правая кнопки мыши
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    col, row = mx // CELL_SIZE, my // CELL_SIZE
                    if event.button == 1:
                        self.board.reveal(row, col)
                    elif event.button == 3:
                        self.board.toggle_flag(row, col)

                # Клавиша R — рестарт
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.board._generate()
                    if hasattr(self.board, 'game_over'):
                        del self.board.game_over

            # После обработки событий проверяем состояние игры
            if getattr(self.board, 'game_over', False):
                print("Game Over! You hit a mine.")
                running = False
            elif self.board.check_win():
                print("Congratulations! You won.")
                running = False

            self._draw()
            pygame.display.flip()

        pygame.quit()

    def _draw(self):
        self.screen.fill(COLORS['border'])
        for r in range(self.board.height):
            for c in range(self.board.width):
                x, y = c * CELL_SIZE, r * CELL_SIZE
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

                if self.board.revealed[r][c]:
                    pygame.draw.rect(self.screen, COLORS['revealed'], rect)
                    val = self.board.numbers[r][c]
                    if val != 0:
                        txt = self.font.render(str(val), True, COLORS['text'])
                        tx = x + (CELL_SIZE - txt.get_width()) // 2
                        ty = y + (CELL_SIZE - txt.get_height()) // 2
                        self.screen.blit(txt, (tx, ty))
                else:
                    pygame.draw.rect(self.screen, COLORS['covered'], rect)
                    if self.board.flagged[r][c]:
                        pygame.draw.circle(
                            self.screen,
                            COLORS['flag'],
                            (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
                            CELL_SIZE // 4
                        )

                pygame.draw.rect(self.screen, COLORS['border'], rect, 1)
