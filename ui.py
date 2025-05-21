import pygame

CELL_SIZE = 32
HEADER_HEIGHT = 40
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
        grid_w = board.width * CELL_SIZE
        grid_h = board.height * CELL_SIZE
        win_w = width or grid_w
        win_h = height or (HEADER_HEIGHT + grid_h)
        self.screen = pygame.display.set_mode((win_w, win_h))
        pygame.display.set_caption("Minesweeper")
        self.font = pygame.font.SysFont(None, CELL_SIZE // 2)
        self.header_font = pygame.font.SysFont(None, HEADER_HEIGHT // 2)
        self.board = board
        self.start_ticks = pygame.time.get_ticks()

    def run(self):
        running = True
        state = "playing"
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if state == "playing":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = event.pos
                        col, row = mx // CELL_SIZE, (my - HEADER_HEIGHT) // CELL_SIZE
                        if 0 <= row < self.board.height:
                            if event.button == 1:
                                self.board.reveal(row, col)
                            elif event.button == 3:
                                self.board.toggle_flag(row, col)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self._restart()
                            state = "playing"
                        elif event.key == pygame.K_q:
                            running = False
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self._restart()
                            state = "playing"
                        elif event.key == pygame.K_q:
                            running = False

            if state == "playing":
                if getattr(self.board, "game_over", False):
                    state = "game_over"
                elif self.board.check_win():
                    state = "win"

            self._draw()
            if state == "game_over":
                self._draw_message("Game Over! R=Restart  Q=Quit")
            elif state == "win":
                self._draw_message("You Won!    R=Restart  Q=Quit")
            pygame.display.flip()

        pygame.quit()

    def _restart(self):
        self.board._generate()
        if hasattr(self.board, "game_over"):
            del self.board.game_over
        self.start_ticks = pygame.time.get_ticks()

    def _draw(self):
        self.screen.fill(COLORS['border'])
        # Header
        header_rect = pygame.Rect(0, 0, self.screen.get_width(), HEADER_HEIGHT)
        pygame.draw.rect(self.screen, COLORS['header_bg'], header_rect)
        elapsed_sec = (pygame.time.get_ticks() - self.start_ticks) // 1000
        timer_surf = self.header_font.render(f"Time: {elapsed_sec}s", True, COLORS['text'])
        self.screen.blit(timer_surf, (10, (HEADER_HEIGHT - timer_surf.get_height()) // 2))
        flags = sum(sum(row) for row in self.board.flagged)
        mines_left = max(self.board.mines - flags, 0)
        mines_surf = self.header_font.render(f"Mines: {mines_left}", True, COLORS['text'])
        self.screen.blit(mines_surf,
                         (self.screen.get_width() - mines_surf.get_width() - 10,
                          (HEADER_HEIGHT - mines_surf.get_height()) // 2))

        # Grid
        for r in range(self.board.height):
            for c in range(self.board.width):
                x, y = c * CELL_SIZE, HEADER_HEIGHT + r * CELL_SIZE
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
                        pygame.draw.circle(self.screen, COLORS['flag'],
                                           (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
                                           CELL_SIZE // 4)
                pygame.draw.rect(self.screen, COLORS['border'], rect, 1)

    def _draw_message(self, text: str):
        s = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        s.fill((0, 0, 0, 180))
        self.screen.blit(s, (0, 0))
        msg_surf = self.font.render(text, True, (255, 255, 255))
        x = (self.screen.get_width() - msg_surf.get_width()) // 2
        y = (self.screen.get_height() - msg_surf.get_height()) // 2
        self.screen.blit(msg_surf, (x, y))
