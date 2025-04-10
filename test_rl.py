# ---LIBRARIES---
import gymnasium as gym
from ParkingEnv import ParkingEnv

# ---TEST---
def test_parking_env():
    '''Test the ParkingEnv class'''
    env = ParkingEnv()
    obs = env.reset()
    print("------------------------------------- \n intital observation: ", obs)

    done = False
    total_reward = 0
    while not done:
        action = env.action_space.sample()
        obs, reward, done = env.step(action)
        total_reward += reward
        print("\n action: ", action, "\n observation: ", obs, "\n reward: ", reward)

    print("\n total reward: ", total_reward, "\n-------------------------------------")
    env.close()

test_parking_env()