# ---LIBRARIES---
import pygame as pg
import random
from settings import *
import math

# ---CLASS---
class Car(pg.sprite.Sprite):
    def __init__(self, x=100, y=100, width=100, height=45):
        '''Constructor of the car class'''

        pg.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.vel = CAR_SPEED
        self.angle = 0
        self.image = CAR_IMG 
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.moving = False
        self.acc = CAR_ACC
        self.max = MAX_SPEED

        # power up properties
        self.power_name = None
        self.power_time = None

        # sound properties
        self.engine_volume = 0.0
        self.engine_sound = engine_sound
        self.engine_channel = engine_channel
        self.engine_channel.set_volume(self.engine_volume)
        self.engine_channel.play(self.engine_sound, loops=-1)

        
    def drive(self):
        '''Drive the car forward'''

        self.x += self.vel * math.cos(math.radians(self.angle))
        self.y += self.vel * math.sin(math.radians(self.angle))
        self._apply_boundaries()
        self.moving = True # car moves to allow rotation
        
    def reverse(self):
        '''Drive the car backwards'''

        self.x -= self.vel * math.cos(math.radians(self.angle))
        self.y -= self.vel * math.sin(math.radians(self.angle))
        self._apply_boundaries()
        self.moving = True # car moves to allow rotation
               
    def rotate(self, left):
        '''Rotate the car'''

        if left:
            self.angle -= CAR_ROTATION # car turns left 
            
        else:
            self.angle += CAR_ROTATION # car turns right
            
    def move(self):
        '''apply changes to the car's position'''

        self.rect.center = (self.x, self.y) # update position of car
    
    def draw(self):
        '''Draw the car on the screen with new position and rotation'''

        rotated_image = pg.transform.rotate(self.image, -self.angle) # rotate image
        new_rect = rotated_image.get_rect(center=self.rect.center) # draw it again
        screen.blit(rotated_image, new_rect.topleft) # blit the image
        
    def handle_inputs(self):
        '''Handle the inputs of the car'''        
        global beep

        self.moving = False
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.drive() # move forward
            self.inc_engine_sound() # play engine sound

        else:
            self.dec_engine_sound()
            
        if keys[pg.K_s]:
            self.reverse() # move backward
            if not beep_channel.get_busy() and sfx > 0:
                beep_channel.play(beep_sound) 
                beep = True
            
        else:
            beep_channel.stop()
            beep = False
        
            
        if self.moving == True:
            if keys[pg.K_a]:
                self.rotate(left=True) # turn left
            if keys[pg.K_d]:
                self.rotate(left=False) # turn right
                
        if keys[pg.K_SPACE]:
            self.apply_powerup_effect()          
                
    def update(self):
        '''apply all effects to the car'''
        
        self.handle_inputs()
        #self.apply_friction()
        self.move()
        self.draw()
        #self.apply_level_effect()

    def _apply_boundaries(self):
        '''Apply boundaries to the car'''

        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH
            
        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT:
            self.y = HEIGHT
            
    def get_car_rect(self):
        '''Get the car's rect after rotation'''

        rotated_image = pg.transform.rotate(self.image, -self.angle) # call the rotated image
        rotated_rect = rotated_image.get_rect(center=(self.x, self.y)) # make new rect
        return rotated_rect # return it
    
    def reset(self):
        '''Reset the car to its original position and direction'''

        self.x, self.y = 100, 100 # original position
        self.angle = 0 # original direction
    
    def inc_engine_sound(self):
        '''Increase the volume of the engine sound'''
            
        if self.moving and not self.engine_channel.get_busy():
            self.engine_channel.play(self.engine_sound, loops=-1)
        
        if self.engine_volume < 1.5:
            self.engine_volume += 0.05
            self.engine_channel.set_volume(self.engine_volume * sfx) 
        

    def dec_engine_sound(self):
        '''Decrease the volume of the engine sound'''
        
        if self.moving and not self.engine_channel.get_busy():
            self.engine_channel.play(self.engine_sound, loops=-1)
        
        if self.engine_volume > 0.0:
            self.engine_volume -= 0.05
            self.engine_channel.set_volume(self.engine_volume * sfx)
        
# Methods that are under development 

    def accelerate(self): # Pedro: recommended me find a solution using vectors instead of scalar for velocity (combination of deaths for easter egg)
        '''Accelerate the car (under development)'''
        
        self.vel += self.acc
              
    def apply_powerup_effect(self):
        '''Apply the power up effect to the car'''

        if self.power_name == None:
            return False
        
        if self.power_name == "speed_boost":
            if self.power_timer == None:
                self.power_timer = pg.time.get_ticks() # start a timer
                self.max += 10 # temporarily increase the max speed
                
            elif pg.time.get_ticks() - self.power_timer >= 10000: # after 10 seconds
                self.max -= 10 # decrease the max speed
                self.power_name = None # remove current power up
                self.power_timer = None # remove timer
            
        elif self.power_name == "ghost":
            pass # to be determined
    
    def randomise_powerup(self):
        '''randomly choose a powerup'''

        powerUp_list = ["speed_boost", "ghost"] # to be determined
        self.power_name = random.choice(powerUp_list)
        
    def apply_level_effect(self):
        '''buffs/debuffs depending on the the current level'''

        if current_level == 1:
            pass # to be determined
        
        elif current_level == 2:
            pass # to be determined
        
        elif current_index == 3:
            pass # to be determined
        
    def apply_friction(self):
        '''Apply friction to the car (under development)'''

        if self.moving == False:
            if self.vel > 0:
                self.vel -= CAR_FRICTION
                if self.vel < 0:
                    self.vel = 0 # stops it from reaching negative
                    
            elif self.vel < 0:
                self.vel += CAR_FRICTION
                if self.vel > 0:
                    self.vel = 0 # stops it from overshooting
                
