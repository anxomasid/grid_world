''' State '''

import numpy
from game_parameters import *

class State:
    def __init__(self, state=START):
        self.board = numpy.zeros(BOARD_LENGTH, BOARD_WIDTH)
        self.state = state
        self.end = False

    def valueReward(self):
        if self.state == WIN:
            self.end = True
            return 1
        elif self.state == LOSE:
            self.end = True
            return -1
        else:
            return 0

    def nextPosition(self, action):
        asdf

    def plotBoard(self):
