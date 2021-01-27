''' Agent '''

# import libraries, variables and classes
import numpy
from game_parameters import *
from state import State

# define Agent class
class Agent:
    def __init_(self):
        self.State = State()
        self.states = []
        self.actions = ['up', 'down', 'right', 'left']
