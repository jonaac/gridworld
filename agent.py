import random
from pylab import *
from tkinter import *

TILE_GOAL = 16

STATE_COUNT = 16
ACTION_COUNT = 4

class Agent():
    def __init__(self):
        """
        Initialize the learning agent.
        """
        self.reset()
        
    def reset(self):
        """
        Resets all agent data.
        """
        self.run = 0
        self.episode = 0
        self.step = 0
        self.Q = zeros((STATE_COUNT, ACTION_COUNT), dtype=float)
        self.returnSum = 0
        self.G = 0
        
    def init_run(self):
        """
        Resets all run data and starts a new run.
        Override this to reset data!
        """
        self.returnSum = 0
        self.run += 1
        self.episode = -1
        self.init_episode()
    
    def init_episode(self):
        """
        Initializes an episode.
        """
        self.G = 0
        self.step = 0
        self.episode += 1

    def do_step(self, S, act):
        """
        Make the agent take a single step. The agent is given its current state
        and a function to call which takes an action and returns a pair of
        (reward, state). Override this!
        Possible actions are:
            0 = go right
            1 = go up
            2 = go left
            3 = go down
        """
        self.step += 1
        
    def init_options(self, master):
        """
        Override this to add options to the agent options panel.
        """
        pass
