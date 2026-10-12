import pygame

class Window:

    def __init__(self, grid):
        pygame.init()
        self.padding = 50
        self.grid = grid
        self.screen = pygame.display.set_mode((grid.width + self.padding*2, grid.width + self.padding*2))
        self.colour = (0, 0, 0)

        pygame.display.set_caption("My Grid")


    def start(self, fps):
        exit = False
        clock = pygame.time.Clock()
        while not exit:
            self.screen.fill(self.colour)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
            self.grid.update()
            self.grid.draw(self.screen, self.padding)
            pygame.display.update()
            clock.tick(fps)