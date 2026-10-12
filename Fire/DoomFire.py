import numpy
import numpy as np

from Fire.Fire import Fire
from Grid import Grid
from Math import Math

class DoomFire(Fire):
    def __init__(self, width, height, rows, cols):
        Grid.__init__(self, width, height, rows, cols)

    colours_values = [
        (np.array((0, 0, 0)), 0),
        (np.array((179, 48, 9)), 8),
        (np.array((196, 88, 6)), 18),
        (np.array((232, 162, 21)), 26),
        (np.array((255, 237, 33)), 32),
        (np.array((255, 255, 255)), 36),
    ]

    def valueToColour(self, value):
        return Math.lerpColours(value, self.colours_values)