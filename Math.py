import numpy

class Math:

    @staticmethod
    def lerpColours(value, colours_values):
        for i in range(len(colours_values)):
            if value <= colours_values[i][1]:
                if i==0:
                    return colours_values[0][0]
                return numpy.add(colours_values[i-1][0], ((value - colours_values[i-1][1]) / (colours_values[i][1] - colours_values[i-1][1]))*(colours_values[i][0]-colours_values[i-1][0]))
        return colours_values[-1][0]
