import pygame


class GameUI:
    def __init__(self, board, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Minesweeper")
        self.board = board

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((0, 0, 0))
            # TODO: отрисовка поля
            pygame.display.flip()
        pygame.quit()
