from random import randint
import numpy

from Grid import Grid

class Water(Grid):
    def __init__(self, width, height, rows, cols):
        Grid.__init__(self, width, height, rows, cols)
        self.lastvalues = self.values.copy()

    def valueToColour(self, value):
        value = max(min(value, 255), 0)
        return (0.1*value, 32 + 0.3*value, 96 + 0.6*value)

    def draw(self, screen, padding):
        v = self.values
        for box in self.boxes:
            i, j = box.x//box.width, box.y//box.height
            slope = v[min(i+1, self.cols-1)][j] - v[max(i-1, 0)][j] + v[i][min(j+1, self.rows-1)] - v[i][max(j-1, 0)]
            box.colour = self.valueToColour(50 + 5*slope + 0.3*v[i][j])
            box.draw(screen, padding)

    def setup(self):
        for _ in range(2):
            ci, cj = randint(5, self.cols-6), randint(5, self.rows-6)
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    self.values[i][j] += 300 * numpy.exp(-((i - ci) ** 2 + (j - cj) ** 2) / 32)
        self.lastvalues = self.values.copy()

    def update(self):
        newvalues = [[0 for _ in range(len(self.values[0]))] for _ in range(len(self.values))]
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                neighbours = 0
                total=0
                if(0<i):
                    neighbours += 1
                    total += self.values[i-1][j]
                if(i<(len(self.values)-1)):
                    neighbours += 1
                    total += self.values[i+1][j]
                if (0<j):
                    neighbours += 1
                    total += self.values[i][j-1]
                if (j<len(self.values[i])-1):
                    neighbours += 1
                    total += self.values[i][j+1]
                newvalues[i][j] = 0.99*((total/neighbours)*2 - self.lastvalues[i][j])
        self.lastvalues = self.values.copy()
        self.values = newvalues.copy()