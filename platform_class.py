import pygame
class platform:
    def __init__(self,bk_image):
        image_width=bk_image.get_width()
        self.background_surface=pygame.Surface((image_width,600))
        self.background_surface.set_colorkey((0,0,0))
    def create_platform(self,X,Y,obstacle_Rect):
        hitbox=pygame.Rect((X,Y,100,10))
        pygame.draw.rect(self.background_surface,(0,255,0),(X+10,Y,100,10))
        obstacle_Rect.append(hitbox)
    def create_ground(self,X,Y,L,H,obstacle_Rect):
        hitbox=pygame.Rect((X,Y,L,H))
        obstacle_Rect.append(hitbox)
    def create_wall(self,X,Y,L,H,wall_Rect,obstacle_Rect):
        wHitbox=pygame.Rect((X-10,Y+10,L,H))
        tHitbox=pygame.Rect((X-10,Y,L,10))
        pygame.draw.rect(self.background_surface,(0,255,0),(X,Y,L,H))
        wall_Rect.append(wHitbox)
        obstacle_Rect.append(tHitbox)