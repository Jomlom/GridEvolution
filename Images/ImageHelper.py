import numpy as np
from PIL import Image

path = "1.png"
gridsize = (100, 100)
wiggleroom = 5

class ImageHelper:

    @staticmethod
    def prepareImage(path, gridsize, wiggleroom):
        img = Image.open(path).convert("RGB")
        quantized = img.quantize(colors=48).convert("RGB")
        scale = min(quantized.size[0] / (gridsize[0]+2*wiggleroom), quantized.size[1] / (gridsize[1]+2*wiggleroom))
        newsize = ((gridsize[0]+2*wiggleroom)*scale, (gridsize[1]+2*wiggleroom)*scale)
        cropped = quantized.crop((
            (quantized.size[0]-newsize[0])/2,
            (quantized.size[1]-newsize[1])/2,
            newsize[0]+(quantized.size[0]-newsize[0])/2,
            newsize[1]+(quantized.size[1]-newsize[1])/2))
        small = cropped.resize((gridsize[0]+2*wiggleroom, gridsize[1]+2*wiggleroom), Image.Resampling.BOX)
        small.save("current.png", "PNG")
        return np.asarray(small)
