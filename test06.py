#使用物件導向
#2顆圓球左右來回

class Ball():
    x=0
    y=0
    size=0
    color=None
    speedx=0
    speedy=0
    
    
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

balla=Ball()
balla.x=20
balla.y=50
balla.size=20
balla.speed=2
balla.color=RED

ballb=Ball()
ballb.x=20
ballb.y=100
ballb.size=20
ballb.speed=3
ballb.color=BLUE

while True:
    #事件處理
    for event in pygame.event.get():
        
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    #狀態更新        
    #計算圓形位置        
    
    if balla.x+balla.size>500 or balla.x-balla.size<0:
        balla.speed*=-1
    balla.x+=balla.speed
    
    if ballb.x+ballb.size>500 or ballb.x-ballb.size<0:
        ballb.speed*=-1
    ballb.x+=ballb.speed    
    #畫面更新
    DISPLAYSURF.fill(BLACK)    
    pygame.draw.circle(DISPLAYSURF, balla.color, (balla.x, balla.y), ballb.size, 0)  #圓心(x,50)， 半徑=20，實心圓
    pygame.draw.circle(DISPLAYSURF, ballb.color, (ballb.x, ballb.y), ballb.size, 0)  #圓心(x,50)， 半徑=20，實心圓
    pygame.display.update()
    
    fpsClock.tick(FPS)