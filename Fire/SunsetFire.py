import numpy
import numpy as np

from Fire.Fire import Fire
from Grid import Grid
from Math import Math

class SunsetFire(Fire):
    def __init__(self, width, height, rows, cols):
        Grid.__init__(self, width, height, rows, cols)

    colours_values = [
        (np.array((0, 0, 0)), 0),
        (np.array((43, 21, 83)), 8),
        (np.array((79, 37, 139)), 14),
        (np.array((126, 38, 75)), 20),
        (np.array((180, 25, 54)), 26),
        (np.array((214, 95, 27)), 28),
        (np.array((244, 173, 47)), 32),
        (np.array((255, 246, 125)), 34),
        (np.array((255, 255, 255)), 36),
    ]

    def valueToColour(self, value):
        return Math.lerpColours(value, self.colours_values)