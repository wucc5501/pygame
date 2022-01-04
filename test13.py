#使用物件導向
#2顆圓球左右來回
#將球置於串列
# 設定顏色
RED = (255,   0,   0)
BLACK=(0, 0, 0)
BLUE=(0, 0, 255)
WHITE=(255, 255, 255)

class Shape():
    def __init__(self, color=WHITE, speedx=0, speedy=0):
        self.color=color
        self.speedx=speedx
        self.speedy=speedy
        
    def update(self, screen):
        pass
    def draw(self, screen):
        pass
    
class Ball(Shape):
    #建構子
    def __init__(self, x, y, size, color=WHITE, speedx=0, speedy=0):  #預設值
        super().__init__(color, speedx, speedy)
        self.x=x
        self.y=y
        self.size=size
                
    def update(self, screen):
        screen_height=screen.get_height() #取得視窗高度
        screen_width=screen.get_width()   #取得視窗寬度
                        
        if self.x+self.size>screen_width or self.x-self.size<0:
            self.speedx*=-1
        if self.y+self.size>screen_height or self.y-self.size<0:
            self.speedy*=-1
            
        self.x+=self.speedx
        self.y+=self.speedy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, 0)

class Block(Shape):
    def __init__(self, x, y, w, h, color=WHITE, speedx=0, speedy=0):
        super().__init__(color, speedx, speedy)
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
        
    def update(self, screen):
        screen_height=screen.get_height() #取得視窗高度
        screen_width=screen.get_width()   #取得視窗寬度
                        
        if self.x+self.w>screen_width or self.x<0:
            self.speedx*=-1
        if self.y+self.h>screen_height or self.y<0:
            self.speedy*=-1
            
        self.x+=self.speedx
        self.y+=self.speedy
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,400))

pygame.display.set_caption('Pygame好好玩')


    
FPS=30
fpsClock = pygame.time.Clock()

balls=[]
balls.append(Ball(x=20, y=50, size=20, speedx=2, speedy=0, color=RED))
balls.append(Ball(x=20, y=100, size=20, speedx=3, color=BLUE))
balls.append(Block(x=20, y=150, w=30, h=40, speedx=5))

while True:
    #事件處理
    for event in pygame.event.get():
        
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    #狀態更新        
    #計算圓形位置
    for ball in balls:
        ball.update(DISPLAYSURF)
            
    #畫面更新
    DISPLAYSURF.fill(BLACK)
    for ball in balls:
        ball.draw(DISPLAYSURF)  
    
    pygame.display.update()
    
    fpsClock.tick(FPS)