from random import randint
from Grid import Grid

class Fire(Grid):
    def __init__(self, width, height, rows, cols):
        Grid.__init__(self, width, height, rows, cols)

    def valueToColor(self, value):
        return (value*7, value*7, value*7)

    def setup(self):
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                self.values[i][j] = 0
            self.values[i][-1] = 36

    def update(self):
        for i in range(len(self.values)):
            for j in range(len(self.values[i])-1):
                self.values[i-randint(0, 1)][j] = max(self.values[i][j+1] - randint(0, 2), 0)
            self.values[i][-1] = 36