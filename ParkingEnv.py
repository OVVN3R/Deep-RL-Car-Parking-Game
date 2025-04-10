# ---LIBRARIES---
from ParkingSpot import ParkingSpot
from Car import Car
from Obstacles import Obstacle, MovingObstacle
from settings import *
import gymnasium as gym # https://gymnasium.farama.org/
from gymnasium import spaces
import numpy as np
import time


# ---ENVIRONMENT---
class ParkingEnv(gym.Env):
    
    metadata = {"render_modes": ["human"],
                "FPS":1}    

    def __init__(self, render):
        '''Constructor of the environment class'''
        super(ParkingEnv, self).__init__() # inherit from gym.Env
        self.car = Car() 
        self.spot = ParkingSpot()
        self.obstacle = Obstacle()
        self.moving_obstacle = MovingObstacle(vertical=True)

        # Actions: 0 = forward, 1 = reverse, 2 = left, 3 = right
        self.action_space = spaces.Discrete(4)

        # Observations: car_x, car_y, car_angle, 
        #               distance_to_spot, distance_to_obstacle
        self.observation_space = spaces.Box(
            low=np.array([0, 0, -180, 0, 0]),
            high=np.array([WIDTH, HEIGHT, 180, WIDTH, WIDTH]),
            dtype=np.float32
        )

        self.start_time = None
        self.render = render

    def reset(self):
        '''Reset the environment'''
        self.car.reset()
        self.spot = ParkingSpot()
        self.obstacle = Obstacle()
        self.moving_obstacle = MovingObstacle()
        self.start_time = time.time()
        return self.get_obs(), {}
    
    def step(self, action):
        '''Actions to take in the environment'''
        if action == 0:
            self.car.drive()

        elif action == 1:
            self.car.reverse()

        elif action == 2:
            self.car.rotate(left=True)

        elif action == 3:
            self.car.rotate(left=False)

        self.car.update()
        self.moving_obstacle.move()

        obs = self.get_obs()
        reward = self.get_reward()
        done = self.new_episode()

        '''
        # check if time > 20
        elapsed_time = time.time() - self.start_time
        if elapsed_time > 10:
            done = True
            reward -= 100'''

        return obs, reward, done, {}

    def get_obs(self):
        '''Get the current observation of the environment'''
        car_x, car_y = self.car.x, self.car.y
        car_angle = self.car.angle
        dis_to_spot = np.hypot(self.spot.x - self.car.x, self.spot.y - self.car.y)
        dis_to_obstacle = np.hypot(self.obstacle.x - self.car.x, self.obstacle.y - self.car.y)

        return [car_x, car_y, car_angle, dis_to_spot, dis_to_obstacle]
    
    def get_reward(self):
        '''calculate the reward for the runnning episode'''

        elapsed_time = time.time() - self.start_time
        if elapsed_time > 10:
            return -100000

        elif self.spot.is_parked(self.car):
            return 100000 # parked
        
        elif self.obstacle.is_hit(self.car) or self.moving_obstacle.is_hit(self.car):
            return -100000 # repeat
        
        else:
            return -1 # penalty for steps
        
    def new_episode(self):
        '''Decides whether to start a new episode or continue'''

        if self.spot.is_parked(self.car):
            return True
        
        elif self.obstacle.is_hit(self.car) or self.moving_obstacle.is_hit(self.car):
            return True
        
        elif elapsed_time > 10:
            return True
        
        else:
            return False
        
    def render(self):
        '''Render the environment'''
        screen.fill(BLACK)
        self.spot.place()
        self.obstacle.place()
        self.moving_obstacle.place()
        self.car.update()
        pg.display.flip()