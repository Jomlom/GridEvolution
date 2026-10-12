import pygame


class Box:
    def __init__(self, colour, x, y, width, height):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen, padding):
        pygame.draw.rect(screen, self.colour, [padding+self.x, padding+self.y, self.width, self.height])