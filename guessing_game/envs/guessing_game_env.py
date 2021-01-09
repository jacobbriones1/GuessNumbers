import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

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
        self.history.append(self.observation)
        if self.observation < 0.01:
            done = True
            self.guess_count +=1
            reward = 1
        else:
            done = False
            self.guess_count +=1
            reward =0
            

        return self.observation,reward, done, { "numbers":self.numbers, "guesses":self.guess_count}

    
    def reset(self, size=3):
        self.size = size
        self.numbers = np.array(
            [self.np_random.uniform(-self.range, self.range) for i in range(self.size)])
        
        self.guess_count = 0
        self.observation = self.MSE([0]*size)
        self.history = [self.observation]
        return self.observation


            
    def render(self, mode='human', close=False):
        #creating a subplot
        
        if plt.gcf()== None:
            fig,ax = plt.subplot(figsize=(10,10))
        else:
            fig = plt.gcf()
            ax = plt.gca()
        plt.ion()
        
        
        xs = [i for i in range(self.guess_count)]
        ys = self.history[:self.guess_count]
        ax.clear()
        ax.plot(xs, ys,'-o')

        plt.xlim([-0.01,self.guess_count])
        plt.xlabel('Time')
        plt.ylabel('error')
        plt.title('MSE of guess')

        plt.show()
        
        
    
    def MSE(self, guess):
        return np.sum((self.numbers-guess)**2)/self.size
    
    
if __name__=='__main__':
    import guessing_game
    import gym
    env = gym.make('NumberGuessing-v0')
    env.reset(3)
    env.step([0,0,0])
    env.render()
