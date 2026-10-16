from Fire import *
from Fire.DoomFire import DoomFire
from Fire.SunsetFire import SunsetFire
from Fire.MagicFlames import MagicFlames
from Grid import Grid
from Water.RainWater import RainWater
from Water.ReflectiveRainWater import ReflectiveRainWater
from Water.Water import Water
from Window import Window
import pygame

window = Window(
    ReflectiveRainWater(500, 500, 100, 100, "Images/1.png")
)

window.start(15)