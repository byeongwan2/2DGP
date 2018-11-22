import random
from pico2d import *
import game_world
import game_framework
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint(0, 600-1), 0
        self.velocityX = 0
        self.velocityY = 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.velocityX = main_state.boy.x_velocity
        self.velocityY = main_state.boy.y_velocity
        self.x -= self.velocityX * game_framework.frame_time
        self.y -= self.velocityY * game_framework.frame_time