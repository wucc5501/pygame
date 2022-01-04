import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,400))

pygame.display.set_caption('Pygame好好玩')

# 設定顏色
RED = (255,   0,   0)
BLACK=(0, 0, 0)

FPS=30
fpsClock = pygame.time.Clock()

x=20

while True:
    #事件處理
    for event in pygame.event.get():
        
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    #狀態更新        
    x+=2
    
    #畫面更新
    DISPLAYSURF.fill(BLACK)    
    pygame.draw.circle(DISPLAYSURF, RED, (x, 50), 20, 0)  #圓心(x,50)， 半徑=20，實心圓
   
    pygame.display.update()
    
    fpsClock.tick(FPS)