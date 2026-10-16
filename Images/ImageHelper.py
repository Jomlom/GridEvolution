import sys

import numpy as np
from PIL import Image
import pygame

path = "1.png"
gridsize = (100, 100)
wiggleroom = 5

# pygame.init()
# screen = pygame.display.set_mode((1000, 1000))
# pygame.display.set_caption("Image Loading")

img = Image.open(path).convert('RGB')
imgsize = img.size
fits = True
scale = int(min(imgsize[0] / (gridsize[0] + (2*wiggleroom)), imgsize[1] / (gridsize[1] + (2*wiggleroom))))
cropimg = img.crop((
    0,
    0,
    (gridsize[0] + 2*wiggleroom)*scale,
    (gridsize[1] + 2*wiggleroom)*scale
))
imgarr = np.asarray(cropimg)
# print(imgarr)
# print(imgarr)
newimgarr = []
for y in range(gridsize[1]+(2*wiggleroom)):
    row = []
    for x in range(gridsize[0]+(2*wiggleroom)):
        samples = []
        for i in range(scale):
            for j in range(scale):
                samples.append(imgarr[(y*scale)+i][(x*scale)+j])
        row.append(np.array(samples).mean(axis=0).astype(np.uint8))
    newimgarr.append(row)

Image.fromarray(np.array(newimgarr)).save("2.png", "PNG")

# image = pygame.image.load("2.png")
#
# imagerect = image.get_rect()
# imagerect.center = ((screen.get_width() / 2), (screen.get_height() / 2))
#
# print(image.get_height(), image.get_width())
#
# while True:
#     screen.fill((0, 0, 0))
#     screen.blit(image, imagerect)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     pygame.display.update()
