#使用物件導向
#2顆圓球左右來回
#加上方法
class Ball():
    #建構子
    def __init__(self, x, y, size, color, speedx, speedy):
        self.x=x
        self.y=y
        self.size=size
        self.color=color
        self.speedx=speedx
        self.speedy=speedy
        
    def update(self, screen):
        screen_height=screen.get_height() #取得視窗高度
        screen_width=screen.get_width()   #取得視窗寬度
        
                
        if self.x+self.size>screen_width or self.x-self.size<0:
            self.speedx*=-1
        if self.y+self.size>screen_height or self.y-self.size<0:
            self.speedy*=-1
            
        self.x+=self.speedx
        self.y+=self.speedy

    
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,400))

pygame.display.set_caption('Pygame好好玩')

# 設定顏色
RED = (255,   0,   0)
BLACK=(0, 0, 0)
BLUE=(0, 0, 255)
    
FPS=30
fpsClock = pygame.time.Clock()

balla=Ball(x=20, y=50, size=20, speedx=2, speedy=0, color=RED)
ballb=Ball(x=20, y=100, size=20, speedx=3, speedy=0, color=BLUE)


while True:
    #事件處理
    for event in pygame.event.get():
        
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    #狀態更新        
    #計算圓形位置        
    balla.update(DISPLAYSURF)
    
    ballb.update(DISPLAYSURF)
        
    #畫面更新
    DISPLAYSURF.fill(BLACK)    
    pygame.draw.circle(DISPLAYSURF, balla.color, (balla.x, balla.y), ballb.size, 0)  #圓心(x,50)， 半徑=20，實心圓
    pygame.draw.circle(DISPLAYSURF, ballb.color, (ballb.x, ballb.y), ballb.size, 0)  #圓心(x,50)， 半徑=20，實心圓
    pygame.display.update()
    
    fpsClock.tick(FPS)