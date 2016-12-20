import random
from pico2d import *

running = None
Rockman = None

class Buster:
    def __init__(self):
        self.image = load_image('Buster.png')

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Rockman:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 2.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    RIGHT_STAND, LEFT_STAND, RIGHT_RUN, LEFT_RUN, RIGHT_RUN_SHOT, LEFT_RUN_SHOT = 0, 1, 2, 3, 4, 5
    RIGHT_STAND_SHOT, LEFT_STAND_SHOT, RIGHT_JUMP, LEFT_JUMP, RIGHT_JUMP_SHOT, LEFT_JUMP_SHOT = 6, 7, 8, 9, 10, 11
    RIGHT_JUMP_RIGHT, LEFT_JUMP_LEFT, RIGHT_JUMP_SHOT_RIGHT, LEFT_JUMP_SHOT_LEFT = 12, 13, 14, 15
    RIGHT_DEAD, LEFT_DEAD = 16, 17

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 3)
        self.total_frames = 0.0
        self.dir = 0
        self.state = self.RIGHT_STAND
        if self.image == None:
            self.image = load_image('Rockman.png')

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:                                                                           # 키 다운일 때
            if event.key == SDLK_RIGHT:                                                                         # 키 다운이고 오른쪽 화살표
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN,):
                    self.state = self.RIGHT_RUN
                    self.dir = 1
                elif self.state in (self.RIGHT_STAND_SHOT, self.LEFT_STAND_SHOT, self.LEFT_RUN_SHOT,):
                    self.state = self.RIGHT_RUN_SHOT
                    self.dir = 1
                elif self.state in (self.RIGHT_JUMP, self.LEFT_JUMP, self.LEFT_JUMP_LEFT):
                    self.state = self.RIGHT_JUMP_RIGHT
                    self.dir = 1
                elif self.state in (self.LEFT_JUMP_SHOT,):
                    self.state = self.RIGHT_JUMP_SHOT
                    self.dir = 0
                elif self.state in (self.RIGHT_JUMP_SHOT, self.LEFT_JUMP_SHOT, self.LEFT_JUMP_SHOT_LEFT):
                    self.state = self.RIGHT_JUMP_SHOT_RIGHT
                    self.dir = 1
            elif event.key == SDLK_LEFT:                                                                        # 키 다운이고 왼쪽 화살표
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN,):
                    self.state = self.LEFT_RUN
                    self.dir = -1
                elif self.state in (self.RIGHT_STAND_SHOT, self.LEFT_STAND_SHOT, self.RIGHT_RUN_SHOT,):
                    self.state = self.LEFT_RUN_SHOT
                    self.dir = -1
                elif self.state in (self.RIGHT_JUMP, self.LEFT_JUMP, self.RIGHT_JUMP_RIGHT):
                    self.state = self.LEFT_JUMP_LEFT
                    self.dir = -1
                elif self.state in (self.RIGHT_JUMP_SHOT,):
                    self.state = self.LEFT_JUMP_SHOT
                    self.dir = 0
                elif self.state in (self.RIGHT_JUMP_SHOT, self.LEFT_JUMP_SHOT, self.RIGHT_JUMP_SHOT_RIGHT):
                    self.state = self.LEFT_JUMP_SHOT_LEFT
                    self.dir = -1
            elif event.key == SDLK_x:                                                                           # 키 다운이고 x키
                if self.state in (self.RIGHT_STAND,):
                    self.state = self.RIGHT_STAND_SHOT
                elif self.state in (self.LEFT_STAND,):
                    self.state = self.LEFT_STAND_SHOT
                elif self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_RUN_SHOT
                elif self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_RUN_SHOT
                elif self.state in (self.RIGHT_JUMP,):
                    self.state = self.RIGHT_JUMP_SHOT
                elif self.state in (self.LEFT_JUMP,):
                    self.state = self.LEFT_JUMP_SHOT
                elif self.state in (self.RIGHT_JUMP_RIGHT,):
                    self.state = self.RIGHT_JUMP_SHOT_RIGHT
                elif self.state in (self.LEFT_JUMP_LEFT,):
                    self.state = self.LEFT_JUMP_SHOT_LEFT
            elif event.key == SDLK_z:                                                                           # 키 다운이고 z키
                if self.state in (self.RIGHT_STAND,):
                    self.state = self.RIGHT_JUMP
                elif self.state in (self.LEFT_STAND,):
                    self.state = self.LEFT_JUMP
                elif self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_JUMP_RIGHT
                elif self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_JUMP_LEFT
                elif self.state in (self.LEFT_JUMP_SHOT,):
                    self.state = self.LEFT_JUMP_SHOT_LEFT
        elif event.type == SDL_KEYUP:                                                                           # 키 업일 때
            if event.key == SDLK_RIGHT:                                                                         # 키 업이고 오른쪽 화살표
                if self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_STAND
                    self.dir = 0
                elif self.state in (self.RIGHT_RUN_SHOT,):
                    self.state = self.RIGHT_STAND_SHOT
                    self.dir = 0
                elif self.state in (self.RIGHT_JUMP_RIGHT,):
                    self.state = self.RIGHT_JUMP
                    self.dir = 0
                elif self.state in (self.RIGHT_JUMP_SHOT_RIGHT,):
                    self.state = self.RIGHT_JUMP_SHOT
                    self.dir = 0
            elif event.key == SDLK_LEFT:                                                                        # 키 업이고 왼쪽 화살표
                if self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_STAND
                    self.dir = 0
                elif self.state in (self.LEFT_RUN_SHOT,):
                    self.state = self.LEFT_STAND_SHOT
                    self.dir = 0
                elif self.state in (self.LEFT_JUMP_LEFT,):
                    self.state = self.LEFT_JUMP
                    self.dir = 0
                elif self.state in (self.LEFT_JUMP_SHOT_LEFT,):
                    self.state = self.LEFT_JUMP_SHOT
                    self.dir = 0
            elif event.key == SDLK_x:                                                                           # 키 업이고 x키
                if self.state in (self.RIGHT_STAND_SHOT,):
                    self.state = self.RIGHT_STAND
                elif self.state in (self.LEFT_STAND_SHOT,):
                    self.state = self.LEFT_STAND
                elif self.state in (self.RIGHT_RUN_SHOT,):
                    self.state = self.RIGHT_RUN
                elif self.state in (self.LEFT_RUN_SHOT,):
                    self.state = self.LEFT_RUN
                elif self.state in (self.RIGHT_JUMP_SHOT,):
                    self.state = self.RIGHT_JUMP
                elif self.state in (self.LEFT_JUMP_SHOT,):
                    self.state = self.LEFT_JUMP
                elif self.state in (self.RIGHT_JUMP_SHOT_RIGHT,):
                    self.state = self.RIGHT_JUMP_RIGHT
                elif self.state in (self.LEFT_JUMP_SHOT_LEFT,):
                    self.state = self.LEFT_JUMP_LEFT
            elif event.key == SDLK_z:                                                                           # 키 업이고 z키
                if self.state in (self.RIGHT_JUMP,):
                    self.state = self.RIGHT_STAND
                elif self.state in (self.LEFT_JUMP,):
                    self.state = self.LEFT_STAND
                elif self.state in (self.RIGHT_JUMP, self.RIGHT_JUMP_RIGHT):
                    self.state = self.RIGHT_RUN
                elif self.state in (self.LEFT_JUMP, self.LEFT_JUMP_LEFT):
                    self.state = self.LEFT_RUN
                elif self.state in (self.RIGHT_JUMP_RIGHT,):
                    self.state = self.RIGHT_JUMP
                elif self.state in (self.LEFT_JUMP_LEFT,):
                    self.state = self.LEFT_JUMP


    def update(self, frame_time):
        distance = Rockman.RUN_SPEED_PPS * frame_time
        self.total_frames += rockman.FRAMES_PER_ACTION * rockman.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)




    def draw(self):
        self.image.clip_draw(self.frame*32, self.state * 30, 32, 30, self.x, self.y)




def handle_events(frame_time):

    global running
    global rockman
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False
        else:
            rockman.handle_events(event)

current_time = 0.0


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def main():

    open_canvas()

    global rockman
    global running

    rockman = Rockman()
    grass = Grass()

    running = True
    current_time = get_time()

    while running:
        frame_time = get_frame_time()
        handle_events(frame_time)
        rockman.update(frame_time)

        clear_canvas()
        grass.draw()
        rockman.draw()
        update_canvas()

    close_canvas()


if __name__ == '__main__':
    main()