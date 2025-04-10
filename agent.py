# ---LIBRARIES---
import numpy as np
import random
from matplotlib import pyplot as plt

# Epsilon-greedy agent
class CarAgent:
    def __init__(self, env, epsilon=1, alpha=0.01, gamma=0.99, 
                 epsilon_decay=0.995, min_epsilon=0.01):
        
        '''Constructor of the agent'''
        self.env = env
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        self.q_table = {}
        self.total_reward = 0
        self.done = False
        self.rewards = []

    def get_state(self, obs):
        '''convert observation to string'''
        return tuple(obs)

    def choose_action(self, state):
        '''choose an action based on strategy'''
        if random.uniform(0, 1) < self.epsilon:
            return self.env.action_space.sample() # explore actions
        
        else:
            return self.get_best_action(state) # exploit learned values
        
    def get_best_action(self, state):
        '''get best action from q-table'''
        if state not in self.q_table:
            self.q_table[state] = np.zeros(self.env.action_space.n)
        
        return np.argmax(self.q_table[state])
    
    def update_table(self, state, next_state, action, reward):
        '''Update q-table with the new values'''
        if state not in self.q_table:
            self.q_table[state] = np.zeros(self.env.action_space.n)
        
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(self.env.action_space.n)


        best_action = self.get_best_action(next_state)
        target = reward + self.gamma * self.q_table[next_state][best_action] # Bellman equation
        error = target - self.q_table[state][action] # TD error (Temporal Difference)
        self.q_table[state][action] += self.alpha * error # Update q-table

    def train(self, episodes=1000):
        '''train agent'''

        plt.ion()
        fig, ax = plt.subplots()


        for episode  in range(episodes):
            state = self.get_state(self.env.reset()[0])
            self.done = False
            self.total_reward = 0

            while not self.done:
                action = self.choose_action(state)
                next_obs, reward, self.done, _ = self.env.step(action)
                next_state = self.get_state(next_obs)
                self.update_table(state, next_state, action, reward)
                state = next_state
                self.total_reward += reward
        
                #print(f"Episode: {episode + 1}, Step: {reward}, Total Reward: {self.total_reward}") # debug steps

            self.rewards.append(self.total_reward)

            # decay epsilon
            self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)

            #print(f"Episode: {episode + 1}, Total Reward: {self.total_reward:.1f}")

            self.plot_rewards(ax)

        plt.ioff()
        plt.show()

    def plot_rewards(self, ax):
        '''update plot after each episode'''
        ax.clear()
        ax.plot(self.rewards, label="Reward per Episode")
        
        # Calculate cumulative reward
        cumulative_rewards = np.cumsum(self.rewards)
        ax.plot(cumulative_rewards, label="Cumulative Reward", linestyle='--')
        
        plt.xlabel("Episodes")
        plt.ylabel("Reward")  
        plt.title("Training Progress")
        plt.legend()
        plt.pause(0.01)