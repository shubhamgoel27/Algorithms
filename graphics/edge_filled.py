# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:16:38 2016

@author: shubham
"""

import pygame
import sys

screen = pygame.display.set_mode((1100,1000))
color = (125,125,125)
background = (250,250,250)
line_color = (180,100,200)
pygame.draw.polygon(screen, line_color, [[300,400],[200,100],[500,400]],3)
pygame.draw.polygon(screen,(80,80,80), [[200,100],[300,400],[1000,400], [1000, 100]])

#(2,1) and (5,4)
pygame.draw.polygon(screen,color, [[200,100],[500,400],[1000,400], [1000, 100]])
#(2,1 and (3,4))


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit()