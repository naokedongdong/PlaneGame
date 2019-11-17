from pygame.locals import *
import pygame

def key_control(hero_obj):
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero_obj.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                hero_obj.move_right()
            elif event.key == K_SPACE:
                hero_obj.fire()
