Welcome to Plane Game!

use A,D or LEFT,Right to control Plane, SPACE for fire.

Good Luck!


#定义你的飞机
class HeroPlane(object):
  def __init__(self,screen_temp):
    self.x=209
    self.y=599
    self.screen = screen_temp
    self.image = pygame.image.load("./feiji/hero0.png")
    self.bullet_list = []

  def display(self):
    self.screen.blit(self.image,(self.x,self.y))
    for bullet in self.bullet_list:
      bullet.display()
      bullet.move()
      if bullet.judge(): #判断子弹是否越界
        self.bullet_list.remove(bullet)

  def move_left(self):
    self.x-=4

  def move_right(self):
    self.x+=4

  def move_up(self):
    self.y-=4

  def move_down(self):
    self.y+=4

  def fire(self):
    self.bullet_list.append(Bullet(self.screen,self.x,self.y))

#定义敌机
class EnemyPlane(object):
  def __init__(self,screen_temp):
    self.x=-1
    self.y=-1
    self.screen = screen_temp
    self.image = pygame.image.load("./feiji/enemy-1.png")
    self.bullet_list = []
    self.direction = "right"

  def display(self):
    self.screen.blit(self.image,(self.x,self.y))
    for bullet in self.bullet_list:
      bullet.display()
      bullet.move()

  def move(self):
    if self.direction == "right" :
       self.x += 2
    elif self.direction == "left" :
       self.x -= 2

    if self.x > 399:
       self.direction = "left"
    elif self.x <= -1:
       self.direction = "right"

  def fire(self):
    random_num = random.randint(0,100)
    if random_num == 29 or random_num == 20:
      self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))

class Bullet(object):
  def __init__(self,screen_temp,x_temp,y_temp):
    self.x=x_temp+39
    self.y=y_temp-21
    self.screen=screen_temp
    self.image=pygame.image.load("./feiji/bullet.png")

  def display(self):
    self.screen.blit(self.image,(self.x,self.y))

  def move(self):
    self.y-=9

  def judge(self):
    if self.y < -1 :
      return True
    else:
      return False

class EnemyBullet(object):
  def __init__(self,screen_temp,x_temp,y_temp):
    self.x=x_temp+24
    self.y=y_temp+41
    self.screen=screen_temp
    self.image=pygame.image.load("./feiji/bullet0.png")

  def display(self):
    self.screen.blit(self.image,(self.x,self.y))

  def move(self):
    self.y+=9

  def judge(self):
    if self.y > 599:
      return True
    else:
      return False
        pygame.init()

  screen = pygame.display.set_mode((480,740),0,32)

  backgroud = pygame.image.load("./feiji/background.png")

  hero = HeroPlane(screen)

  #创建敌机
  enemy=EnemyPlane(screen)

  while True:

    screen.blit(backgroud,(0,0))

    hero.display()

    enemy.display()
    enemy.move()
    enemy.fire()

    pygame.display.update()

    key_control(hero)

    time.sleep(0.01)
