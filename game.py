import pygame
from main_menu import *
from level_1 import *
running=True
current_screen="main_menu"
pygame.init()
clock=pygame.time.Clock()
level_1_finish=False
main_menu_startup=False
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if current_screen=="main_menu":
        if main_menu_startup==False:
            main_menu()
            main_menu_startup=True
        main_menu_loop()
        current_screen=main_menu_screen_return()
        level_1_startup=False
    elif current_screen=="level_1":
        if level_1_startup==False:
            level_1()
            level_1_startup=True
        level_1_loop()
        level_1_finish=level_1_finish_var()
        main_menu_startup=False
    if level_1_finish==True:
       current_screen="main_menu"
       level_1_finish=False
    clock.tick(30)
    