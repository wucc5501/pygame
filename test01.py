#pygame基本架構

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))

pygame.display.set_caption('Pygame好好玩')

while True:
    
    #事件處理
    for event in pygame.event.get():
        
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
    #狀態更新
            
    #畫面更新
    
    
    pygame.display.update()