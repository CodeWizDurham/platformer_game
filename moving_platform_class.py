import pygame
class moving_platform:
    def __init__(self,bk_image,index,current_X,current_Y,slide_coordinate_L,slide_coordinate_R):
        self.current_X=current_X
        self.current_Y=current_Y
        self.spawn_X=current_X
        self.index=index
        self.Rect=0
        self.slide_coordinate_L=slide_coordinate_L
        self.slide_coordinate_R=slide_coordinate_R
        image_width=bk_image.get_width()
        self.background_surface=pygame.Surface((image_width,600))
        self.background_surface.set_colorkey((0,0,0))
        self.move=-1
    def movement_update(self,player_step,move_obstacle_Rect):
        self.background_surface.fill("black")
        self.hitbox_slide(player_step)
        self.Rect=pygame.Rect((self.current_X-10,self.current_Y,100,10))
        move_obstacle_Rect[self.index]=self.Rect
        pygame.draw.rect(self.background_surface,(105,105,105),(self.spawn_X,self.current_Y,100,10))
        self.back_forth()
    def back_forth(self):
        self.current_X-=self.move
        self.spawn_X-=self.move
        if self.current_X<=self.slide_coordinate_L:
            self.move=-1
        elif self.current_X>=self.slide_coordinate_R:
            self.move=1
    def hitbox_slide(self,player_step):
        self.current_X-=player_step
        self.slide_coordinate_L-=player_step
        self.slide_coordinate_R-=player_step