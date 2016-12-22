import random

from pico2d import *

class Stairtop:
    def __init__(self):
        pass
    def draw(self):
        self.image.draw(400, 300)

    def get_bb(self):
        return 675, 89, 800, 90

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

