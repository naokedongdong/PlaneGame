# -*- coding=utf-8 -*-

import pygame
import random

#屏幕边框大小
SCREEN_SIZE = (480, 852)
PLANE_SIZE = (100, 124)
ENEMY_SIZE = (51, 39)

#基础类
class Base(object):
    def __init__(self, x, y, screen, image):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

#定义英雄飞机类
class HeroPlane(Base):

    #定义hero移动的步长
    HERO_STEP = 10

    def __init__(self, x, y, screen, image):
        Base.__init__(self, x, y, screen, image)
        self.bullet_list = []

    def display(self):
        Base.display(self)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move_left(self):
        #定义左边界
        if self.x - HeroPlane.HERO_STEP >= 0:
            self.x = self.x - HeroPlane.HERO_STEP
        else:
            pass

    def move_right(self):
        #定义右边界
        if self.x + HeroPlane.HERO_STEP <= SCREEN_SIZE[0] - PLANE_SIZE[0] :
            self.x = self.x + HeroPlane.HERO_STEP
        else:
            pass

    def fire(self):
        bullet_x = self.x + PLANE_SIZE[0]/2 - 8
        bullet_y = self.y - 10
        self.bullet_list.append(HeroBullet(bullet_x, bullet_y, self.screen))


#定义敌机类
class EnemyPlane(Base):

    #定义敌机步长
    ENEMY_STEP = 5
    def __init__(self, x, y, screen, image):
        Base.__init__(self, x, y, screen, image)
        self.direction = 1  #默认往右
        self.bullet_list = []

    def display(self):
        Base.display(self)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move(self):
        boundary = (0,SCREEN_SIZE[0]-ENEMY_SIZE[0])
        if self.direction == 1:
            self.x += EnemyPlane.ENEMY_STEP
        else:
            self.x -= EnemyPlane.ENEMY_STEP

        if self.x > boundary[1]:
            self.direction = 0
        elif self.x < boundary[0]:
            self.direction = 1

    def fire(self):
        ran_num = random.randint(0,100)
        if ran_num == 20 or ran_num == 80 :
            self.bullet_list.append(EnemyBullet(self.x, self.y, self.screen))



#定义hero子弹
class HeroBullet(Base):
    #定义子弹步长
    BULLET_STEP = 7

    def __init__(self, x, y, screen):
        Base.__init__(self, x, y, screen, "/Users/Sander/python/PlaneGame/pic/bullet.png")

    def display(self):
        Base.display(self)

    def move(self):
        self.y -= HeroBullet.BULLET_STEP

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

#定义enemy子弹
class EnemyBullet(Base):
    #定义子弹步长
    BULLET_STEP = 7

    def __init__(self, x, y, screen):
        Base.__init__(self, x, y, screen, "/Users/Sander/python/PlaneGame/pic/bullet1.png")

    def display(self):
        Base.display(self)

    def move(self):
        self.y += HeroBullet.BULLET_STEP

    def judge(self):
        if self.y > SCREEN_SIZE[1]:
            return True
        else:
            return False
