# Example file showing a basic pygame "game loop"
import pygame
from draw_circle import *
from sprite_sprite import *
from constants import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.time.set_timer(COUNTDOWN, CLOCK)

while running:
    # poll for events
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if my_sprite.rect.collidepoint(event.pos):
                my_sprite.onclick()

        elif event.type == COUNTDOWN:
            print("try again")
            all_sprites.draw(screen)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    

    #my_circle.draw_circle(screen)

    all_sprites.draw(screen)



    # flip() the display to put your work on screen


    pygame.display.flip()


    

    clock.tick(60)  # limits FPS to 60

pygame.quit()