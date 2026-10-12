import random

from Box import Box

class Grid:

    def valueToColor(self, value):
        return(0, 0, 0)

    def draw(self, screen, padding):
        for box in self.boxes:
            box.colour = self.valueToColor(self.values[box.x//box.width][box.y//box.height])
            box.draw(screen, padding)

    def update(self):
        pass

    def setup(self):
        pass

    def __init__(self, width, height, rows, cols):
        self.boxes = []
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.values = [[0 for _ in range(cols)] for _ in range(rows)]

        boxheight = height // rows
        boxwidth = width // cols
        for i in range(rows):
            for j in range(cols):
                self.boxes.append(Box(
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    j*boxwidth, i*boxheight,
                    boxwidth, boxheight
                ))

        self.setup()