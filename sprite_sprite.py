import pygame
from constants import *
from draw_circle import random_num_gen

class click_my_sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def onclick(self):
        print("sprite clicked up")

my_sprite = click_my_sprite(COLOR, WIDTH, HEIGHT, random_num_gen(), random_num_gen())
all_sprites = pygame.sprite.Group(my_sprite)