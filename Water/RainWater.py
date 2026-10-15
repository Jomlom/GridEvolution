from random import randint
import numpy

from Water.Water import Water


class RainWater(Water):

    def __init__(self, width, height, rows, cols):
        super().__init__(width, height, rows, cols)

    def setup(self):
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                self.values[i][j] = 100
        self.lastvalues = self.values.copy()

    def update(self):
        newvalues = [[0 for _ in range(len(self.values))] for _ in range(len(self.values[0]))]
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
                newvalues[i][j] = 0.85*((total/neighbours)*2 - self.lastvalues[i][j])
                if randint(1, 2000) == 1:
                    for i2 in range(len(self.values)):
                        for j2 in range(len(self.values[i])):
                            newvalues[i2][j2] += 100 * numpy.exp(-((i2 - i) ** 2 + (j2 - j) ** 2) / randint(2,8))
        self.lastvalues = self.values.copy()
        self.values = newvalues.copy()