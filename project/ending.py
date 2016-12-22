import game_framework
from pico2d import *

name = "EndingState"

image = None
logo_time = 0.0


def enter():
    global image
    open_canvas()
    image = load_image('ending.png')


def exit():
    global image
    del(image)
    close_canvas()


def update(frame_time):
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        game_framework.quit()
    delay(0.01)
    logo_time += 0.01


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()




def handle_events(frame_time):
    pass


def pause(): pass


def resume(): pass