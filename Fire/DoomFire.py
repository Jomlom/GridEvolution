import numpy

from Fire.Fire import Fire
from Grid import Grid

class DoomFire(Fire):
    def __init__(self, width, height, rows, cols):
        Grid.__init__(self, width, height, rows, cols)

    def valueToColor(self, value):
        if value == 0:
            return (0, 0, 0)
        elif 0 < value <= 8:
            return (value/8)*numpy.array((179, 48, 9))
        elif 8 < value <= 18:
            return numpy.add((179, 48, 9), ((value-8)/10)*(numpy.subtract((196, 88, 6),(179, 48, 9))))
        elif 18 < value <= 26:
            return numpy.add((196, 88, 6), ((value-18)/8)*(numpy.subtract((232, 162, 21),(196, 88, 6))))
        elif 26 < value <= 32:
            return numpy.add((232, 162, 21), ((value-26)/6)*(numpy.subtract((255, 237, 33),(232, 162, 21))))
        elif 32 < value < 36:
            return numpy.add((255, 237, 33), ((value-32)/3)*(numpy.subtract((255, 255, 255),(255, 237, 33))))
        else:
            return (255, 255, 255)