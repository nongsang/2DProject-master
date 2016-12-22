from pico2d import *

import game_framework
import ending


from test_rockman import Boy # import Boy class from boy.py
from test_niddle import Niddle
from test_goal import Goal




name = "test_stage1"

boy = None
niddle = None
goal = None


def create_world():
    global boy, niddle, goal

    boy = Boy()
    niddle = Niddle()
    goal = Goal()


def destroy_world():
    global boy, niddle, goal


    del(boy)
    del(niddle)
    del(goal)


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

    if collide(boy, niddle):
        boy.stopy()
        boy.y = 80
    if collide(boy, goal):
        game_framework.change_state(ending)




def draw(frame_time):
    clear_canvas()
    niddle.draw()
    boy.draw()



    niddle.draw_bb()
    boy.draw_bb()
    goal.draw_bb()


    update_canvas()






