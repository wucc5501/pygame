#2顆圓球左右來回
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

x1=20
y1=50
size1=20
speed1=2
color1=RED

x2=20
y2=100
size2=20
speed2=3
color2=BLUE

while True:
    #事件處理
    for event in pygame.event.get():
        
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    #狀態更新        
    #計算圓形位置        
    
    if x1+size1>500 or x1-size1<0:
        speed1*=-1
    x1+=speed1
    
    if x2+size2>500 or x2-size2<0:
        speed2*=-1
    x2+=speed2    
    #畫面更新
    DISPLAYSURF.fill(BLACK)    
    pygame.draw.circle(DISPLAYSURF, color1, (x1, y1), size1, 0)  #圓心(x,50)， 半徑=20，實心圓
    pygame.draw.circle(DISPLAYSURF, color2, (x2, y2), size2, 0)  #圓心(x,50)， 半徑=20，實心圓
    pygame.display.update()
    
    fpsClock.tick(FPS)