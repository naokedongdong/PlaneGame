from pygame.locals import *
import pygame

SCREEN_SIZE = (480, 852)
PLANE_SIZE = (100, 124)
ENEMY_SIZE = (51, 39)
PLANE_BULLET_SIZE = (22, 22)
ENEMY_BULLET_SIZE = (9, 21)

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

def if_shot(hero, ememy):
    for bullet in ememy.bullet_list:
        if hero.x < bullet.x < hero.x + PLANE_SIZE[0] and hero.y < bullet.y < hero.y + PLANE_SIZE[1]:
            return True
        else:
            return False

