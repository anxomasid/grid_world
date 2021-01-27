''' State '''

# import libraries and variables
import numpy
from game_parameters import *

# define State class
class State:

    def __init__(self, state=START, input_step=INPUT_STEP):
        self.board = numpy.zeros(BOARD_LENGTH, BOARD_WIDTH)
        self.state = state
        self.endGame = False
        self.inputStep = INPUT_STEP

    def valueReward(self):
        if self.state == WIN:
            self.endGame = True
            return 1
        elif self.state == LOSE:
            self.endGame= True
            return -1
        else:
            return 0

    def nextPosition(self, action):
        'Falta checkear OBSTACLES y INPUT_STEP'
        if action == 'up':
            nextState = (self.State[0], self.State[1] + 1)
        elif action == 'down':
            nextState = (self.State[0], self.State[1] - 1)
        elif action == 'right':
            nextState = (self.State[0] + 1, self.State[1])
        elif action == 'left':
            nextState = (self.State[0] - 1, self.State[1])
        elif action == 'up-right':
            nextState = (self.State[0] + 1, self.State[1] + 1)
        elif action == 'up-left':
            nextState = (self.State[0] + 1, self.State[1] - 1)
        elif action == 'down-right':
            nextState = (self.State[0] + 1, self.State[1] - 1)
        elif action == 'down-left':
            nextState = (self.State[0] - 1, self.State[1] - 1)
        return nextState

    def plotBoard(self):
        'Falta función de plot'
