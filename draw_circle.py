import pygame
import random
from constants import *

class circle:
    def __init__(self, color):
        #self.pos_x = pos_x
        #self.pos_y = pos_y
        self.color = color
        self.radius = 50

    def draw_circle(self, screen):
        pygame.draw.circle(screen, color=self.color, center=(random_num_gen(), random_num_gen()), radius=self.radius)
        pygame.time.delay(1000)
        
def random_num_gen():
    x = random.randrange(500)
    return x



my_circle = circle(COLOR)



        