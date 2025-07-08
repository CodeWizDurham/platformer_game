from platform_class import *
from class_Enemies import *
from player_class import *
from moving_platform_class import *
import pygame
def level_1():
    pygame.init()
    
    global screen
    global obstacle_Rect
    global move_obstacle_Rect
    global enemy_rect
    global character
    global Level_1
    global background_X
    global platform_builder
    global walker
    global wall_rect
    screen=pygame.display.set_mode((600,600))
    background_X=-10
    Level_1=pygame.image.load("level_1.png").convert()
    character=player("pass",10,10,"pass","wood sword","pass","pass","pass","pass","pass","pass",300,450,background_X,screen)
    walker=enemy("pass",2,2,7,"walker","none",0,pygame.Rect((1400,500,250,10)),"pass","pass","pass","pass","pass","pass",1475,490,screen)
    platform_builder=platform(Level_1)
    obstacle_Rect=[]
    move_obstacle_Rect=[]
    enemy_rect=[]
    wall_rect=[]
    enemies=[walker]
    moving_platforms=[]
    for enemything in enemies:
        enemy_rect.append(0)
    for moving_platformthing in moving_platforms:
        move_obstacle_Rect.append(0)
    platform_builder.create_ground(35,500,4130,100,obstacle_Rect)
    platform_builder.create_platform(500,400,obstacle_Rect)
    platform_builder.create_wall(700,400,200,100,wall_rect,obstacle_Rect)
    platform_builder.create_platform(975,250,obstacle_Rect)
    platform_builder.create_wall(1200,300,100,200,wall_rect,obstacle_Rect)
    
    print("hello")
def level_1_loop():
    for event in pygame.event.get(): #quits game
        if event.type==pygame.QUIT:
            pygame.quit
    global background_X
    screen.blit(Level_1,(background_X,0)) #loads images
    screen.blit(platform_builder.background_surface,(background_X,0))
    background_X=character.movement_Update(obstacle_Rect,wall_rect,move_obstacle_Rect,enemy_rect) #updates character movement
    walker.movement_Update(obstacle_Rect,enemy_rect,character.step,character.Rect)
    walker.health_Update(character.damage,character.enemy_attacked,enemy_rect,False)
    character.health_Update(walker.enemy_Attack())
    
    global finish_var #checks if finished
    finish_var=character.finish(-2200)
    #if finish_var==True:
        #pass
    #clock.tick(30)
    pygame.display.update()
    #pygame.quit()
def level_1_finish_var():
    return finish_var