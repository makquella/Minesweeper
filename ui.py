import pygame

CELL_SIZE = 32
HEADER_HEIGHT = 40   # высота области для таймера и счётчика мин

COLORS = {
    'covered':  (192, 192, 192),
    'revealed': (224, 224, 224),
    'flag':     (255, 0, 0),
    'mine':     (0, 0, 0),
    'text':     (0, 0, 255),
    'border':   (0, 0, 0),
    'header_bg': (200, 200, 200),
}


class GameUI:
    def __init__(self, board, width=None, height=None):
        pygame.init()

        # количество пикселей сетки
        grid_w = board.width * CELL_SIZE
        grid_h = board.height * CELL_SIZE

        # итоговые размеры окна: над сеткой область для заголовка
        win_w = width or grid_w
        win_h = height or (HEADER_HEIGHT + grid_h)

        self.screen = pygame.display.set_mode((win_w, win_h))
        pygame.display.set_caption("Minesweeper")

        self.font = pygame.font.SysFont(None, CELL_SIZE // 2)
        self.header_font = pygame.font.SysFont(None, HEADER_HEIGHT // 2)

        self.board = board
        # Запомним, когда стартовала игра
        self.start_ticks = pygame.time.get_ticks()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Левая и правая кнопки мыши
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    # Если кликнули в области заголовка — игнорируем
                    if my < HEADER_HEIGHT:
                        continue

                    col = mx // CELL_SIZE
                    row = (my - HEADER_HEIGHT) // CELL_SIZE
                    if 0 <= row < self.board.height and 0 <= col < self.board.width:
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

        # 1) Рисуем фон заголовка
        header_rect = pygame.Rect(0, 0, self.screen.get_width(), HEADER_HEIGHT)
        pygame.draw.rect(self.screen, COLORS['header_bg'], header_rect)

        # 2) Рисуем таймер (секунды с начала)
        elapsed_ms = pygame.time.get_ticks() - self.start_ticks
        elapsed_sec = elapsed_ms // 1000
        timer_surf = self.header_font.render(f"Time: {elapsed_sec}s", True, COLORS['text'])
        self.screen.blit(timer_surf, (10, (HEADER_HEIGHT - timer_surf.get_height()) // 2))

        # 3) Рисуем счётчик оставшихся мин
        # посчитаем, сколько флажков установлено
        flags = sum(sum(1 for cell in row if cell) for row in self.board.flagged)
        mines_left = max(self.board.mines - flags, 0)
        mines_surf = self.header_font.render(f"Mines: {mines_left}", True, COLORS['text'])
        # справа отступ 10px
        x_pos = self.screen.get_width() - mines_surf.get_width() - 10
        self.screen.blit(mines_surf, (x_pos, (HEADER_HEIGHT - mines_surf.get_height()) // 2))

        # 4) Рисуем сетку со смещением по Y = HEADER_HEIGHT
        for r in range(self.board.height):
            for c in range(self.board.width):
                x = c * CELL_SIZE
                y = HEADER_HEIGHT + r * CELL_SIZE
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
