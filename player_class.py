import pygame
class player:
    def __init__(self,picture,health,max_health,armour,weapon,death_Animation,death_Sound,attack_Sound,movement_Sound,attack_Animation,movement_Animation,spawn_X,spawn_Y,background_X,screen):
        self.picture=picture
        self.weapon=weapon
        self.health=health
        self.armour=armour
        self.death_Animation=death_Animation
        self.death_Sound=death_Sound
        self.attack_Sound=attack_Sound
        self.movement_Sound=movement_Sound
        self.attack_Animation=attack_Animation
        self.movement_Animation=movement_Animation
        self.spawn_X=spawn_X
        self.spawn_Y=spawn_Y
        self.current_X=spawn_X
        self.current_Y=spawn_Y
        self.screen=screen
        self.fall_Speed=0
        self.gravity=1.5
        self.screen_Height=700
        self.character_Height=20
        self.jump_Cooldown=False
        self.background_X=background_X
        self.Rect=pygame.Rect(self.current_X,self.current_Y,20,20)
        self.step=0
        self.temp_x=0
        self.attack_Cooldown=0
        self.damage=0
        self.enemy_attacked="none"
        self.facing="Right"
        self.collide_Wall_left=False
        self.collide_Wall_right=False
        self.velocity=0
        self.collided_wall=0
        self.max_health=max_health
        self.heal_cooldown=200
        
    def movement_Update(self,obstacle_Rect,wall_Rect,move_obstacle_Rect,enemy_Rect):
        self.Rect=pygame.Rect(self.current_X,self.current_Y,20,20)
        self.enemy_attacked="none"
        #self.player_Attack(enemy_Rect)
        self.temp_x=self.current_X
        keys=pygame.key.get_pressed()
        if self.attack_Cooldown<=0:

            if keys[pygame.K_SPACE]:

                if self.weapon=="wood sword":

                    if self.facing=="Right":
                        self.sword=pygame.Rect(self.current_X+10,self.current_Y-30,30,40)
                        pygame.draw.rect(self.screen,(0,0,255),(self.current_X+10,self.current_Y-30,30,30))

                    elif self.facing=="Left":
                        self.sword=pygame.Rect(self.current_X-20,self.current_Y-30,30,40)
                        pygame.draw.rect(self.screen,(0,0,255),(self.current_X-20,self.current_Y-30,30,30))
                    
                    #print("hi")
                    for x in range(len(enemy_Rect)):
                        #print(enemy_hitbox)
                        #print(self.sword)
                        if self.sword.colliderect(enemy_Rect[x])==True:
                            self.damage=3
                            self.enemy_attacked=x
                            #print(x)
                            #print(self.enemy_attacked)
                        
                            
                self.attack_Cooldown+=50
                
        else:
            self.attack_Cooldown-=1
            self.damage=0

        if (keys[pygame.K_LEFT]or keys[pygame.K_a])and self.current_X>35 and self.collide_Wall_right==False:
            self.collide_Wall_left=False
            self.velocity=-5
            self.current_X+=self.velocity
            self.facing="Left"

        if (keys[pygame.K_RIGHT]or keys[pygame.K_d])and self.current_X<545 and self.collide_Wall_left==False:
            self.collide_Wall_right=False
            self.velocity=5
            self.current_X+=self.velocity
            self.facing="Right"

        if (keys[pygame.K_UP]or keys[pygame.K_w])and self.jump_Cooldown==False:
            self.jump_Cooldown=True
            self.fall_Speed=-21.5
            
                

        else:
            
            if self.detect_Collision(obstacle_Rect,move_obstacle_Rect):

                if self.fall_Speed!=0:
                    self.fall_Speed=0

            else:
                self.fall_Speed+=self.gravity
        self.detect_wall_collision(wall_Rect)
        self.side_Scrolling(obstacle_Rect,wall_Rect)
        self.current_Y+=self.fall_Speed
        pygame.draw.rect(self.screen,(101,67,33),(self.current_X,self.current_Y-20,20,20))
        return self.background_X
    


    def side_Scrolling(self,obstacle_Rect,wall_Rect):
        if self.current_X<300 and self.background_X<0 and self.temp_x!=self.current_X:
            self.current_X+=5
            self.background_X+=5
            self.hitbox_slide(-5,obstacle_Rect,wall_Rect)

        elif self.current_X>300 and self.background_X>-3600 and self.temp_x!=self.current_X:
            self.current_X-=5
            self.background_X-=5
            self.hitbox_slide(5,obstacle_Rect,wall_Rect)

        else:
            self.hitbox_slide(0,obstacle_Rect,wall_Rect)



    def detect_Collision(self,obstacle_Rect,move_obstacle_Rect):
        for bounding_Box in obstacle_Rect+move_obstacle_Rect: 
            if self.Rect.colliderect(bounding_Box)==True:

                self.jump_Cooldown=False
                self.current_Y=bounding_Box.top
                return True
            


            '''
            if bounding_Box.top==self.Rect[1] and bounding_Box.left<=self.Rect.right and bounding_Box.right>=self.Rect.left:
                self.jump_Cooldown=False
                self.current_Y=bounding_Box.top
                return True
            elif bounding_Box.top>self.Rect[1] and bounding_Box.left<=self.Rect.right:
                self.collide_Wall_left=True
                self.collide_Wall_right=False
            elif bounding_Box.top>self.Rect[1] and bounding_Box.right>=self.Rect.left:
                self.collide_Wall_right=True
                self.collide_Wall_left=False
            else:
                self.collide_Wall_right=False
                self.collide_Wall_left=False
            '''
    def detect_wall_collision(self,wall_Rect):
        #self.collide_Wall_left=False
        #self.collide_Wall_left=False
        for bounding_Box in wall_Rect:
            #print(bounding_Box)
            #print(self.Rect)
            if self.Rect.colliderect(bounding_Box)==True:

                #print("hi, i'm working")
                #print(f"{self.velocity}=velocity")
                #print(f"{bounding_Box.top}=bounding_Box.top")
                #print(f"{self.Rect[1]}=self.Rect")
                self.collided_wall=bounding_Box
                if self.velocity==-5 and bounding_Box.top+10<self.Rect[1]:
                    self.collide_Wall_right=True
                    self.current_X=bounding_Box.right
                    self.collide_Wall_left=False

                elif self.velocity==5 and bounding_Box.top+10<self.Rect[1]:
                    self.collide_Wall_left=True
                    self.current_X=bounding_Box.left-20
                    self.collide_Wall_right=False
                #elif bounding_Box.top>=self.Rect[1]
            if self.collided_wall!=0:
                if self.collided_wall.top+10>self.Rect[1]:
                    self.collide_Wall_left=False
                    self.collide_Wall_right=False

    def health_Update(self,enemy_Attack):
        self.health-=enemy_Attack
        print(self.heal_cooldown)
        if enemy_Attack>0:
            self.heal_cooldown=200
        elif self.heal_cooldown<=0 and self.health<self.max_health:
            self.health+=1
            self.heal_cooldown=200
        else:
            self.heal_cooldown-=1
        font=pygame.font.SysFont("calibri",40)
        text=font.render(str(self.health),True,(255,0,0))
        self.screen.blit(text,(10,10))
        if self.health<=0:
            pygame.quit()



    def hitbox_slide(self,step,obstacle_Rect,wall_Rect):
        self.step=step
        for hitbox in obstacle_Rect:
            hitbox[0]-=step

        for hitbox in wall_Rect:
            hitbox[0]-=step



    def position_Reference(self):
        return pygame.Rect(self.current_X,self.current_Y,20,20)
    


    def finish(self,finish):
        if self.background_X<=finish:
            return(True)
        
        else:
            return(False)