# Example file showing a basic pygame "game loop"
import pygame
import sys
from draw_circle import *
from constants import *


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
from sprite_sprite import *
clock = pygame.time.Clock()
running = True
pygame.time.set_timer(COUNTDOWN, CLOCK)

life_hearts = 5

class lives_left:
    def __init__(self, life):
        self.life = life     

    def loose_a_life(self):
        self.life -= 1
        return self

lives = lives_left(life_hearts)


times_hit_target = 0

#pygame.font.Font(lives, size=12)

while running:
    # poll for events
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if my_sprite.rect.collidepoint(event.pos):
                my_sprite.onclick()
                my_sprite.move_sprite()
                times_hit_target += 1

        elif event.type == COUNTDOWN:
            lives.loose_a_life()
            print(life_hearts)
            if life_hearts == 0:
                print("YOU LOSE")
                print(f"You hit the target {times_hit_target} times")
                running = False
                sys.exit()
            else:
                print(f"You have {life_hearts} lives left")
        
            
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    

    #my_circle.draw_circle(screen)

    all_sprites.draw(screen)



    # flip() the display to put your work on screen


    pygame.display.flip()


    

    clock.tick(60)  # limits FPS to 60

pygame.quit()