from Fire import Fire
from Fire.DoomFire import DoomFire
from Grid import Grid
from Window import Window
import pygame

window = Window(
    DoomFire(500, 500, 50, 50)
)

window.start()