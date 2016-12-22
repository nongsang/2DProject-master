import random

from pico2d import *

class Goal:
    def __init__(self):
        pass

    def draw(self):
        pass

    def get_bb(self):
        return 700, 440, 732, 473

    def draw_bb(self):
        draw_rectangle(*self.get_bb())