#使用物件導向
#2顆圓球左右來回
#建構子
class Ball():
    #建構子
    def __init__(self, x, y, size, color, speedx, speedy):
        self.x=x
        self.y=y
        self.size=size
        self.color=color
        self.speedx=speedx
        self.speedy=speedy
    
    
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
    if balla.x+balla.size>500 or balla.x-balla.size<0:
        balla.speedx*=-1
    balla.x+=balla.speedx
    
    if ballb.x+ballb.size>500 or ballb.x-ballb.size<0:
        ballb.speedx*=-1
    ballb.x+=ballb.speedx    
    #畫面更新
    DISPLAYSURF.fill(BLACK)    
    pygame.draw.circle(DISPLAYSURF, balla.color, (balla.x, balla.y), ballb.size, 0)  #圓心(x,50)， 半徑=20，實心圓
    pygame.draw.circle(DISPLAYSURF, ballb.color, (ballb.x, ballb.y), ballb.size, 0)  #圓心(x,50)， 半徑=20，實心圓
    pygame.display.update()
    
    fpsClock.tick(FPS)