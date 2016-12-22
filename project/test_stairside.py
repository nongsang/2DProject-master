import random

from pico2d import *

class Stairside:
    def __init__(self):
        pass

    def draw(self):
        self.image.draw(400, 300)

    def get_bb(self):
        return 671, 20, 672, 85

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

