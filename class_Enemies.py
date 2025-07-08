import pygame
class enemy:
    def __init__(self,picture,speed,damage,health,type,armour,index,hitbox,death_Animation,death_Sound,attack_Sound,movement_Sound,attack_Animation,movement_Animation,spawn_X,spawn_Y,screen):
        self.picture=picture
        self.speed=speed
        self.damage=damage
        self.health=health
        self.type=type
        self.armour=armour
        self.glowing=False
        self.death_Animation=death_Animation
        self.death_Sound=death_Sound
        self.attack_Sound=attack_Sound
        self.movement_Sound=movement_Sound
        self.attack_Animation=attack_Animation
        self.movement_Animation=movement_Animation
        self.screen=screen
        self.cooldown=0
        self.spawn_X=spawn_X
        self.spawn_Y=spawn_Y
        self.current_X=spawn_X
        self.current_Y=spawn_Y
        self.Rect=0
        self.hitbox=hitbox
        self.enemy_index=0
        self.spawn_index=index
        self.death=False
        self.fall_speed=0
        self.gravity=0.5
        self.fall_timer=0
        self.player_Position=0
        self.see=False
        self.startup=False


    def health_Update(self,player_attack,enemy_attacked,enemy_rect,glowing):
        #if enemy_attacked!="none":
            #print(enemy_attacked)
        #print(self.index)
        if (self.type=="hopper"or"runner"or"walker"or"archer") and enemy_attacked==self.spawn_index:
            
            #print("enemy attacked")
            #print(f"{self.type} attacked")
            #print(f"enemy index {self.index}")
            #print("dmg"+str(player_attack))
            if self.armour=="leather":
                self.health-=player_attack/2
            elif self.armour=="iron":
                self.health-=player_attack/3
            elif self.armour=="gold":
                self.health-=player_attack/4
            else:
                self.health-=player_attack
                #print("hp"+str(self.health))
            #print(self.health)
            if self.health<=0 and self.death!=True:
                self.Rect=pygame.Rect((-1000,-1000,10,10))
                self.death=True
                #print(len(enemy_rect))
        elif self.type=="healer":
            if glowing==True:
                self.health+=player_attack
            elif glowing==False:
                if self.armour=="leather":
                    self.health-=player_attack/2
                elif self.armour=="iron":
                    self.health-=player_attack/3
                elif self.armour=="gold":
                    self.health-=player_attack/4
                else:
                    self.health-=player_attack
            if self.health<=0:
                pass #death animation
        #add boss types later



    def movement_Update(self,obstacle_Rect,enemy_Rect,player_step,player_Position):
        self.player_Position=player_Position
        if self.death==False:
            self.Rect=pygame.Rect((self.current_X,self.current_Y+11,10,10))
            if self.startup==False:
                #print(f"startup {self.type}")
                enemy_Rect[self.spawn_index]=self.Rect
                self.screen_Rect=self.Rect
                #print(enemy_Rect[self.spawn_index])
                self.startup=True
            #print(enemy_Rect)
            #print(self.Rect)
            #print(self.type)
            #self.enemy_index=enemy_Rect.index(self.screen_Rect)
            #print(self.enemy_index)
            enemy_Rect[self.spawn_index]=self.Rect
            pygame.draw.rect(self.screen,(255,0,0),(self.current_X,self.current_Y,10,10))
            self.screen_Rect=self.Rect
            if self.type=="runner":
                self.chase()
            if self.type!="runner":
                self.back_Forth(obstacle_Rect)
            self.hitbox_slide(player_step)
    def back_Forth(self,obstacle_Rect):
        
        if self.Rect.colliderect(self.hitbox)==True:
            self.fall_speed=0
            
            #print(self.hitbox)
            self.current_Y=self.hitbox.top-10
            
            self.current_X+=self.speed
            if self.hitbox.left>=self.Rect.left:
                self.speed=self.speed*-1
                self.current_X+=abs(self.speed)+2
            elif self.hitbox.right<=self.Rect.right:
                self.speed=self.speed*-1
                self.current_X-=abs(self.speed)+2
        if self.type=="hopper":
            if self.fall_timer<=0:
                self.current_Y-=10
                self.fall_speed=-12
                self.fall_timer=50
            else:
                self.fall_timer-=1
            self.fall_speed+=self.gravity
            self.current_Y+=self.fall_speed
            self.current_Y=max(0,min(self.current_Y,490))
    def chase(self):
        if self.player_Position[1]>=self.Rect[1]-100:
            if self.player_Position.left<=self.Rect.right+125 and self.player_Position.right>=self.Rect.left-125:
                self.see=True
        if self.see==True:
            if self.Rect[0]-self.player_Position[0]<0:
                self.current_X+=self.speed
            elif self.Rect[0]-self.player_Position[0]>0:
                self.current_X-=self.speed
    def enemy_Attack(self):
        if self.cooldown<=0 and self.death!=True:
            #print(self.Rect)
            #print(player_Position)
            #print(self.Rect.colliderect(player_Position))
            if self.Rect.colliderect(self.player_Position)==True:
                self.cooldown+=50
                return self.damage
            else:
                return 0
        else:
            self.cooldown-=1
            return 0
    def hitbox_slide(self,player_step):
        self.current_X-=player_step
        self.hitbox[0]-=player_step