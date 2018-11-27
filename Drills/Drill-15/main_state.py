import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import world_build_state
import rank_state
from zombie import Zombie
name = "MainState"
rank = None
final_rank = None

def collide(a, b):

    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

boy = None

def enter():
    global rank

    with open('rank_data.json', 'rt') as f:
        rank = json.load(f)


    global boy
    boy = world_build_state.get_boy()
    pass

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()
        else:
            boy.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()
        if isinstance(game_object, Zombie):
            if collide(boy,game_object):
                rank.append(round(boy.survival_time,2))
                rank.sort()
                rank.reverse()
                with open('rank_data.json', 'wt') as f:
                    json.dump(rank, f)
                game_framework.change_state(rank_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()


    update_canvas()






