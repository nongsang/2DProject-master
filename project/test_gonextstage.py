import random

from pico2d import *

class Gotonextstage2:
    def __init__(self):
        pass

    def draw(self):
        pass

    def get_bb(self):
        return 799, 90, 800, 600

    def draw_bb(self):
        draw_rectangle(*self.get_bb())