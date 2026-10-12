import random

from Box import Box
from Grid import Grid

class MagicFlames(Grid):

    def __init__(self, width, height, rows, cols):
        self.boxes = []
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.values1 = [[0 for _ in range(cols)] for _ in range(rows)]
        self.values2 = [[0 for _ in range(cols)] for _ in range(rows)]
        self.values3 = [[0 for _ in range(cols)] for _ in range(rows)]

        boxheight = height // rows
        boxwidth = width // cols
        for i in range(rows):
            for j in range(cols):
                self.boxes.append(Box(
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    j * boxwidth, i * boxheight,
                    boxwidth, boxheight
                ))

        self.setup()

    def draw(self, screen, padding):
        for box in self.boxes:
            box.colour = self.valueToColour((
                self.values1[box.x//box.width][box.y//box.height],
                self.values2[box.x//box.width][box.y//box.height],
                self.values3[box.x//box.width][box.y//box.height]
            ))
            box.draw(screen, padding)

    def valueToColour(self, values):
        return ((values[0]+values[1])*2, (values[1]+values[2])*2, (values[2]+values[0])*3)

    def setup(self):
        for i in range(len(self.values1)):
            for j in range(len(self.values1[i])):
                self.values1[i][j] = 0
            self.values1[i][-1] = 36
        for i in range(len(self.values2)):
            for j in range(len(self.values2[i])):
                self.values2[i][j] = 0
            self.values2[i][-1] = 36
        for i in range(len(self.values3)):
            for j in range(len(self.values3[i])):
                self.values3[i][j] = 0
            self.values3[i][-1] = 36

    def update(self):
        for i in range(len(self.values1)):
            for j in range(len(self.values1[i])-1):
                self.values1[i - random.randint(0, 1)][j] = max(self.values1[i][j + 1] - random.randint(0, 2), 0)
            self.values1[i][-1] = 36
        for i in range(len(self.values2)):
            for j in range(len(self.values2[i])-1):
                self.values2[i - random.randint(0, 1)][j] = max(self.values2[i][j + 1] - random.randint(0, 2), 0)
            self.values2[i][-1] = 36
        for i in range(len(self.values3)):
            for j in range(len(self.values3[i])-1):
                self.values3[-(i - random.randint(0, 2))][j] = max(self.values3[-i][j + 1] - random.randint(0, 2), 0)
            self.values3[i][-1] = 36