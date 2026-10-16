from random import randint
import numpy

from Images.ImageHelper import ImageHelper
from Water.RainWater import RainWater

class ReflectiveRainWater(RainWater):

    def __init__(self, width, height, rows, cols, imgpath):
        super().__init__(width, height, rows, cols)
        self.wiggleroom = 5
        self.image = ImageHelper.prepareImage(imgpath, (cols, rows), self.wiggleroom)

    def valuesLocationToColour(self, slopex, slopey, x, y):
        xadjust = slopex/3
        xadjust = round(min((max(-self.wiggleroom, xadjust), self.wiggleroom)))
        yadjust = slopey/3
        yadjust = round(min((max(-self.wiggleroom, yadjust), self.wiggleroom)))
        return (self.image[y+self.wiggleroom+yadjust][x+self.wiggleroom+xadjust])

    def draw(self, screen, padding):
        v = self.values
        for box in self.boxes:
            i, j = box.x//box.width, box.y//box.height
            slopex = v[min(i+1, self.cols-1)][j] - v[max(i-1, 0)][j]
            slopey = v[i][min(j+1, self.rows-1)] - v[i][max(j-1, 0)]
            box.colour = self.valuesLocationToColour(slopex, slopey, i, j)
            box.draw(screen, padding)

    def setup(self):
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                self.values[i][j] = 100
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
                newvalues[i][j] = 0.85*((total/neighbours)*2 - self.lastvalues[i][j])
                if randint(1, 2000) == 1:
                    for i2 in range(len(self.values)):
                        for j2 in range(len(self.values[i])):
                            newvalues[i2][j2] -= 100 * numpy.exp(-((i2 - i) ** 2 + (j2 - j) ** 2) / randint(2,8))
        self.lastvalues = self.values.copy()
        self.values = newvalues.copy()