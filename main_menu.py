import pygame
from level_debug import *
from level_1 import *
def main_menu():
    pygame.init()
    global screen
    global level_select
    global level_select_stat
    global current_screen
    screen=pygame.display.set_mode((600,600))
    screen.fill((135,206,255))
    pygame.draw.rect(screen,(0,255,0),(200,350,200,50))
    font_title=pygame.font.Font("Grand9K Pixel.ttf",50)
    font_button=pygame.font.Font("Grand9K Pixel.ttf",35)
    text_title=font_title.render("Platformer Game",True,(0,0,0))
    text_button=font_button.render("Play",True,(0,0,0))
    level_select=pygame.image.load("level_select.png").convert()
    level_select.set_colorkey((255,255,255))
    screen.blit(text_title,(100,200))
    screen.blit(text_button,(260,345))
    level_select_stat=False
    current_screen="main_menu"
def main_menu_loop():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    global level_select_stat
    global current_screen
    keys=pygame.key.get_pressed()
    mouse_pos=pygame.mouse.get_pos()
    if keys[pygame.K_LCTRL] and keys[pygame.K_BACKSLASH]:
        level_debug()
    if pygame.mouse.get_pressed()[0] and mouse_pos[0]>=200 and mouse_pos[0]<=400 and mouse_pos[1]>=350 and mouse_pos[1]<=400 and level_select_stat==False:
        screen.fill((135,206,255))
        screen.blit(level_select,(0,0))
        level_select_stat=True
    if pygame.mouse.get_pressed()[0] and mouse_pos[0]>=37 and mouse_pos[0]<=295 and mouse_pos[1]>=160 and mouse_pos[1]<=216 and level_select_stat:
        current_screen="level_1"
        
    #clock.tick(30)                                                                                                                                                                                                                                                                                                                                                                                                   
    pygame.display.update()
    #pygame.quit()
def main_menu_screen_return():
    return current_screen