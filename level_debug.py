from platform_class import *
from class_Enemies import *
from player_class import *
from moving_platform_class import *
import pygame
def level_debug():
    pygame.init()
    
    screen=pygame.display.set_mode((600,600))
    clock=pygame.time.Clock()
    background_X=-10
    running=True
    Level_debug=pygame.image.load("Level_debug.png").convert()
    character=player("pass",10,"pass","wood sword","pass","pass","pass","pass","pass","pass",300,450,background_X,screen)
    walker=enemy("pass",2,2,7,"walker","none",0,"pass","pass","pass","pass","pass","pass",260,380,screen)
    hopper=enemy("pass",3,3,5,"hopper","none",1,"pass","pass","pass","pass","pass","pass",760,380,screen)
    runner=enemy("pass",3,5,3,"runner","none",2,"pass","pass","pass","pass","pass","pass",500,490,screen)
    platform_builder=platform(Level_debug)
    moving_platform1=moving_platform(Level_debug,0,500,390,400,600)
    obstacle_Rect=[]
    move_obstacle_Rect=[]
    enemy_rect=[]
    enemies=[walker,hopper,runner]
    moving_platforms=[moving_platform1]
    for enemything in enemies:
        enemy_rect.append(0)
    for moving_platformthing in moving_platforms:
        move_obstacle_Rect.append(0)
    platform_builder.create_ground(35,500,4130,100,obstacle_Rect)
    platform_builder.create_platform(240,390,obstacle_Rect)
    platform_builder.create_platform(740,390,obstacle_Rect)
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.blit(Level_debug,(background_X,0))
        screen.blit(platform_builder.background_surface,(background_X,0))
        screen.blit(moving_platform1.background_surface,(background_X,0))
        #print(obstacle_Rect)
        moving_platform1.movement_update(character.step,move_obstacle_Rect)
        background_X=character.movement_Update(obstacle_Rect,move_obstacle_Rect,enemy_rect)
        walker.movement_Update(obstacle_Rect,enemy_rect,character.step,character.Rect)
        walker.health_Update(character.damage,character.enemy_attacked,enemy_rect,False)
        hopper.movement_Update(obstacle_Rect,enemy_rect,character.step,character.Rect)
        hopper.health_Update(character.damage,character.enemy_attacked,enemy_rect,False)
        runner.movement_Update(obstacle_Rect,enemy_rect,character.step,character.Rect)
        runner.health_Update(character.damage,character.enemy_attacked,enemy_rect,False)
        character.health_Update(walker.enemy_Attack())
        character.health_Update(hopper.enemy_Attack())
        character.health_Update(runner.enemy_Attack())
        clock.tick(30)
        pygame.display.update()
    pygame.quit()