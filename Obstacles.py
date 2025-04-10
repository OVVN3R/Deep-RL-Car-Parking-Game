# ---LIBRARIES---
import pygame as pg
from settings import *

# ---CLASS---
class Obstacle(pg.sprite.Sprite):
    
    def __init__(self, x=300, y=300, width=100, height=100):
        '''constructor to initialise the obstacle'''

        pg.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.image = OBSTACLE_IMG
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.ghost = False
        
    def place(self):
        '''places the obstacle on the screen'''
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)
        
    def is_hit(self, car):
        '''checks if the car collides with the obstacle'''        

        car_rect = car.get_car_rect()

        # use pixel perfect collision using msks
        car_mask = pg.mask.from_surface(pg.transform.rotate(car.image, -car.angle))
        obstacle_mask = pg.mask.from_surface(self.image)
        
        # offsets between the car and obstacle
        x = self.rect.left - car_rect.left
        y = self.rect.top - car_rect.top
        
        # if there's any overlap between the masks
        return car_mask.overlap(obstacle_mask, (x, y))
    
    def penalty(self, car):
        '''penalises the car when it collides with the obstacle'''

        if self.is_hit(car):
            car.reset() # reset position of car
            print("--------------------------") # test collision
            if sfx > 0:
                crash_channel.play(crash_sound)
            
                                 
    def test_for_obstacle(self, car):
        '''tests if the car collides with the obstacle'''

        if self.is_hit(car): # Tests if the car collides the obstacle
            print("True")
            
        else:
            print("False")

# under development
    def ghost_active(self):
        '''activates powerup (under development)'''
        pass
        

# ---SUBCLASS---
class MovingObstacle(Obstacle):
    def __init__(self, x=300, y=300, width=100, height=100, vertical=False):
        '''constructor to initialise the moving obstacle'''

        super().__init__(x=300, y=300, width=100, height=100)
        self.speed = OBSTACLE_SPEED
        self.vertical = vertical
        
    def move(self):
        '''moves the obstacle'''

        if self.vertical:
            self.y += self.speed # move vertically
            if self.y <= 0 or self.y >= HEIGHT: # when center hits boundary it bounce
                self.speed = -self.speed # positive becomes negative and visa versa
        else:
            self.x += self.speed # move horizontally
            if self.x <= 0 or self.x >= WIDTH: # when center hits boundary it bounce
                self.speed = -self.speed # positive becomes negative and visa versa
                
        self.rect.center = (self.x, self.y)
        
    def place(self):
        '''places the moving obstacle on the screen'''

        self.move()
        screen.blit(self.image, self.rect)
            

