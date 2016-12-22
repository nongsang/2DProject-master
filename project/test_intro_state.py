import game_framework
from pico2d import *
import test_stage1

name = "IntroState"
image = None


def enter():
    global image
    image = load_image('intro.png')


def exit():
    global image
    del(image)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
               game_framework.push_state(test_stage1)



def draw(frame_time):
    clear_canvas()
    image.draw(400, 300)
    update_canvas()







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass