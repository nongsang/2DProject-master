import random

from pico2d import *

class Map:
    def __init__(self):
        self.image = load_image('map.png')

    def draw(self):
        self.image.draw(400, 300)

    def get_bb(self):
        return 0, 0, 800, 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

