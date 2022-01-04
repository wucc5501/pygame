import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,400))

pygame.display.set_caption('Pygame好好玩')

# 設定顏色
RED = (255,   0,   0)


x=300
while True:
        
    #事件處理
    for event in pygame.event.get():
        
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    #狀態更新
            
    #畫面更新
    pygame.draw.circle(DISPLAYSURF, RED, (300, 50), 20, 0) #圓心(300,50)， 半徑=20，實心圓        
        
    pygame.display.update()