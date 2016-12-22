import random

from pico2d import *

class Boy:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    RIGHT_STAND, LEFT_STAND, RIGHT_RUN, LEFT_RUN, RIGHT_RUN_SHOT, LEFT_RUN_SHOT = 0, 1, 2, 3, 4, 5
    RIGHT_STAND_SHOT, LEFT_STAND_SHOT, RIGHT_JUMP, LEFT_JUMP, RIGHT_JUMP_SHOT, LEFT_JUMP_SHOT = 6, 7, 8, 9, 10, 11
    RIGHT_JUMP_RIGHT, LEFT_JUMP_LEFT, RIGHT_JUMP_SHOT_RIGHT, LEFT_JUMP_SHOT_LEFT, DEAD = 12, 13, 14, 15, 16

    def __init__(self):
        self.x, self.y = 40,80
        self.frame = random.randint(0, 3)
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0
        self.state = self.RIGHT_STAND
        if self.image == None:
            self.image = load_image('Rockman.png')


    def update(self, frame_time):
        def clampx(minimumx, x, maximumx):
            return max(minimumx, min(x, maximumx))
        def clampy(minimumy, y, maximumy):
            return max(minimumy, min(y, maximumy))

        distance = self.RUN_SPEED_PPS * frame_time
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        self.x += (self.xdir * distance)
        self.y += (self.ydir * distance)

        self.x = clampx(16, self.x, 784)
        self.y = clampy(15, self.y, 585)


    def draw(self):
        self.image.clip_draw(self.frame * 32, self.state * 30, 32, 30, self.x, self.y)

    def stopy(self):
        self.ydir = 0

    def stopx(self):
        self.xdir = 0

    def get_bb(self):
        return self.x - 16, self.y - 15, self.x + 16, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:                                                                           # 키 다운일 때
            if event.key == SDLK_RIGHT:                                                                         # 키 다운이고 오른쪽 화살표
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN,):
                    self.state = self.RIGHT_RUN
                    self.xdir = 1
                elif self.state in (self.RIGHT_STAND_SHOT, self.LEFT_STAND_SHOT, self.LEFT_RUN_SHOT,):
                    self.state = self.RIGHT_RUN_SHOT
                    self.xdir = 1
                elif self.state in (self.RIGHT_JUMP, self.LEFT_JUMP, self.LEFT_JUMP_LEFT):
                    self.state = self.RIGHT_JUMP_RIGHT
                    self.xdir = 1
                elif self.state in (self.LEFT_JUMP_SHOT,):
                    self.state = self.RIGHT_JUMP_SHOT
                    self.xdir = 0
                elif self.state in (self.RIGHT_JUMP_SHOT, self.LEFT_JUMP_SHOT, self.LEFT_JUMP_SHOT_LEFT):
                    self.state = self.RIGHT_JUMP_SHOT_RIGHT
                    self.xdir = 1
            elif event.key == SDLK_LEFT:                                                                        # 키 다운이고 왼쪽 화살표
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN,):
                    self.state = self.LEFT_RUN
                    self.xdir = -1
                elif self.state in (self.RIGHT_STAND_SHOT, self.LEFT_STAND_SHOT, self.RIGHT_RUN_SHOT,):
                    self.state = self.LEFT_RUN_SHOT
                    self.xdir = -1
                elif self.state in (self.RIGHT_JUMP, self.LEFT_JUMP, self.RIGHT_JUMP_RIGHT):
                    self.state = self.LEFT_JUMP_LEFT
                    self.xdir = -1
                elif self.state in (self.RIGHT_JUMP_SHOT,):
                    self.state = self.LEFT_JUMP_SHOT
                    self.xdir = 0
                elif self.state in (self.RIGHT_JUMP_SHOT, self.LEFT_JUMP_SHOT, self.RIGHT_JUMP_SHOT_RIGHT):
                    self.state = self.LEFT_JUMP_SHOT_LEFT
                    self.xdir = -1
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
                    self.ydir = 1
                elif self.state in (self.LEFT_STAND,):
                    self.state = self.LEFT_JUMP
                    self.ydir = 1
                elif self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_JUMP_RIGHT
                    self.ydir = 1
                elif self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_JUMP_LEFT
                    self.ydir = 1
                elif self.state in (self.LEFT_JUMP_SHOT,):
                    self.state = self.LEFT_JUMP_SHOT_LEFT
                    self.ydir = 1
                elif self.state in (self.RIGHT_STAND_SHOT,):
                    self.state = self.RIGHT_JUMP_SHOT
                    self.ydir = 1
                elif self.state in (self.LEFT_STAND_SHOT,):
                    self.state = self.LEFT_JUMP_SHOT
                    self.ydir = 1
                elif self.state in (self.RIGHT_RUN_SHOT,):
                    self.state = self.RIGHT_JUMP_SHOT_RIGHT
                    self.ydir = 1
                elif self.state in (self.LEFT_RUN_SHOT,):
                    self.state = self.LEFT_JUMP_SHOT_LEFT
                    self.ydir = 1
        elif event.type == SDL_KEYUP:                                                                           # 키 업일 때
            if event.key == SDLK_RIGHT:                                                                         # 키 업이고 오른쪽 화살표
                if self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_STAND
                    self.xdir = 0
                elif self.state in (self.RIGHT_RUN_SHOT,):
                    self.state = self.RIGHT_STAND_SHOT
                    self.xdir = 0
                elif self.state in (self.RIGHT_JUMP_RIGHT,):
                    self.state = self.RIGHT_JUMP
                    self.xdir = 0
                elif self.state in (self.RIGHT_JUMP_SHOT_RIGHT,):
                    self.state = self.RIGHT_JUMP_SHOT
                    self.xdir = 0
            elif event.key == SDLK_LEFT:                                                                        # 키 업이고 왼쪽 화살표
                if self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_STAND
                    self.xdir = 0
                elif self.state in (self.LEFT_RUN_SHOT,):
                    self.state = self.LEFT_STAND_SHOT
                    self.xdir = 0
                elif self.state in (self.LEFT_JUMP_LEFT,):
                    self.state = self.LEFT_JUMP
                    self.xdir = 0
                elif self.state in (self.LEFT_JUMP_SHOT_LEFT,):
                    self.state = self.LEFT_JUMP_SHOT
                    self.xdir = 0
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
                    self.ydir = -1
                elif self.state in (self.LEFT_JUMP,):
                    self.state = self.LEFT_STAND
                    self.ydir = -1
                elif self.state in (self.RIGHT_JUMP, self.RIGHT_JUMP_RIGHT):
                    self.state = self.RIGHT_RUN
                    self.ydir = -1
                elif self.state in (self.LEFT_JUMP, self.LEFT_JUMP_LEFT):
                    self.state = self.LEFT_RUN
                    self.ydir = -1
                elif self.state in (self.RIGHT_JUMP_RIGHT,):
                    self.state = self.RIGHT_JUMP
                    self.ydir = -1
                elif self.state in (self.LEFT_JUMP_LEFT,):
                    self.state = self.LEFT_JUMP
                    self.ydir = -1
                elif self.state in (self.RIGHT_JUMP_SHOT,):
                    self.state = self.RIGHT_STAND_SHOT
                    self.ydir = -1
                elif self.state in (self.LEFT_JUMP_SHOT,):
                    self.state = self.LEFT_STAND_SHOT
                    self.ydir = -1
                elif self.state in (self.RIGHT_JUMP_SHOT_RIGHT,):
                    self.state = self.RIGHT_RUN_SHOT
                    self.ydir = -1
                elif self.state in (self.LEFT_JUMP_SHOT_LEFT,):
                    self.state = self.LEFT_RUN_SHOT
                    self.ydir = -1





