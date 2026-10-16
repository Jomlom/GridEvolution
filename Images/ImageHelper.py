import numpy as np
from PIL import Image

path = "1.png"
gridsize = (100, 100)
wiggleroom = 5

class ImageHelper:

    @staticmethod
    def prepareImage(path, gridsize, wiggleroom):
        img = Image.open(path).convert("RGB")
        small = img.resize((gridsize[0]+2*wiggleroom, gridsize[1]+2*wiggleroom), Image.Resampling.BOX)
        quantized = small.quantize(colors=32).convert("RGB")
        quantized.save("current.png", "PNG")
        return np.asarray(quantized)
