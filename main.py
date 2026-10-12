from Fire import Fire
from Fire.DoomFire import DoomFire
from Fire.SunsetFire import SunsetFire
from Fire.MagicFlames import MagicFlames
from Grid import Grid
from Window import Window
import pygame

window = Window(
    SunsetFire(500, 500, 100, 100)
)

window.start(15)