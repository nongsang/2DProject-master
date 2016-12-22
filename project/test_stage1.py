from pico2d import *

import game_framework


from test_rockman import Boy # import Boy class from boy.py
from test_grass import Map
from test_stairtop import Stairtop
from test_stairside import Stairside
from test_gonextstage import Gotonextstage2
import test_stage2



name = "test_stage1"

boy = None
map = None
stairtop = None
stairside = None
gotonextstage2 = None

def create_world():
    global boy, map, stairtop, stairside, gotonextstage2

    boy = Boy()
    map = Map()
    stairtop = Stairtop()
    stairside = Stairside()
    gotonextstage2 = Gotonextstage2()


def destroy_world():
    global boy, map, stairtop, stairside, gotonextstage2


    del(boy)
    del(map)
    del(stairtop)
    del(stairside)
    del(gotonextstage2)


def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def update(frame_time):
    boy.update(frame_time)

    if collide(boy, map):
        boy.stopy()
        boy.y = 36
    if collide(boy, stairtop):
        boy.stopy()
        if collide(boy, stairtop) == False:
            boy.ydir = -1
    if collide(boy, stairside):
        boy.stopx()
        boy.x = 672
    if collide(boy, gotonextstage2):
        game_framework.change_state(test_stage2)




def draw(frame_time):
    clear_canvas()
    map.draw()
    boy.draw()



    map.draw_bb()
    boy.draw_bb()
    stairtop.draw_bb()
    stairside.draw_bb()
    gotonextstage2.draw_bb()


    update_canvas()






