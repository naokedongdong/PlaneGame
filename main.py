# -*- coding:utf-8 -*-

import os
from PIL import Image
import pygame
import time
from BaseClass import *
from BaseFunc import *

from pygame.locals import *

#常量
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

#main函数
def main():

     #图片位置定义和解析
     image_path = PROJECT_PATH + "/pic/"
     BAC_IMAGE = image_path + "background.png"
     HERO_IMAGE = image_path + "hero1.png"
     ENEMY_IMAGE = image_path + "enemy0.png"
     HERO_BULLET_IMAGE = image_path + "bullet.png"
     ENEMY_BULLET_IMAGE = image_path + "bullet1.png"

     #图片大小解析
     bac_image_size = Image.open(BAC_IMAGE).size
     hero_image_size = Image.open(HERO_IMAGE).size
     enemy_image_size = Image.open(ENEMY_IMAGE).size

     #初始化窗口
     pygame.init()
     screen = pygame.display.set_mode(bac_image_size,0,32)
     background = pygame.image.load(BAC_IMAGE)

     #定义hero plane
     hero_pos = ((bac_image_size[0]-hero_image_size[0])/2, (bac_image_size[1]-hero_image_size[1]))
     hero = HeroPlane(hero_pos[0], hero_pos[1], screen, HERO_IMAGE)

     #定义enemy plane
     enemy = EnemyPlane(0, 0, screen, ENEMY_IMAGE)

     while True:
          #加载背景图片
          screen.blit(background,(0,0))

          #加载hero plane
          if if_shot(hero, enemy):
               hero.image = pygame.image.load("/Users/Sander/python/PlaneGame/pic/hero_blowup_n1.png")
               hero.display()
               print("GET SHOT!!!")
               enemy.display()
               enemy.move()
          hero.display()
          key_control(hero)

          #加载敌机
          enemy.display()
          enemy.move()
          enemy.fire()

          #更新窗口，并sleep 0.01s
          pygame.display.update()
          time.sleep(0.01)


if __name__ == "__main__":
    
     main()
