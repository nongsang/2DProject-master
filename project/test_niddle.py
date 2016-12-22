import random

from pico2d import *

class Niddle:
    def __init__(self):
        self.image = load_image('niddle.png')

    def draw(self):
        self.image.draw(400, 300)

    def get_bb(self):
        return 0, 34, 125, 65

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

