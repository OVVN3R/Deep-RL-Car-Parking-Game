# ---LIBRARIES---
import pygame as pg # https://kidscancode.org/lessons/
from settings import *
from random import randint

# ---CLASS---
class ParkingSpot(pg.sprite.Sprite):
    def __init__(self):
        '''constructor to initialise the parking spot'''

        pg.sprite.Sprite.__init__(self)
        self.x, self.y = 600, 100
        self.width, self.height = 125, 65
        self.color = "GREEN"
        self.image = pg.Surface((self.width, self.height), pg.SRCALPHA)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def place(self):
        '''places the parking spot on the screen'''

        screen.blit(self.image, self.rect)
        
    def is_parked(self, car):
        '''checks if the car is parked in the parking spot'''
        
        return self.rect.contains(car.get_car_rect()) # true if the car is inside]
    
    def test_for_parking(self, car):
        '''tests if the car is parked in the parking spot'''

        if self.is_parked(car): # Tests if the car is inside parking spot
            print("TRUE")
            
        else:
            print("FALSE")
        
    def random_position(self):
        '''randomises the position of the parking spot'''
        
        self.x = randint(50, WIDTH - (self.width) - 50)
        self.y = randint(50, HEIGHT - (self.height) - 50)
        self.rect.center = (self.x, self.y)