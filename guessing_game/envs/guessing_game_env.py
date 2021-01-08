import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np


class GuessingGameEnv(gym.Env):
    metadata = {'render.modes':['human']}
    def __init__(self, size=3):
        self.size=size
        self.numbers = np.zeros(size)
        self.range = 100.
        self.seed()
        self.reset()
        
        
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    
    def step(self, action):
        if isinstance(action, list):
            if len(action) == self.size:
                self.action = np.array(action)
            
        
        elif isinstance(action, np.ndarray):
            if action.shape[0]== self.size:
                self.action = action
        
        self.observation = self.MSE(action)
        
        if self.observation < 0.01:
            done = False
            self.guess_count +=1
            reward = 0
        else:
            done = True
            self.guess_count +=1
            reward =1
            

        return self.observation,reward, done, { "numbers":self.numbers, "guesses":self.guess_count}
    
    def reset(self, size=3):
        self.size = size
        self.numbers = np.array(
            [self.np_random.uniform(-self.range, self.range) for i in range(self.size)])
        
        self.guess_count = 0
        self.observation = 0
        return self.observation
    
    def render(self, mode='human', close=False):
        print('Error: ', self.observation)
    
    def MSE(self, guess):
        return np.sum((self.numbers-guess)**2)/self.size
    
    