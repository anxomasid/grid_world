''' State '''

import numpy
from parameters import *

class State:

    def __init__(self, state=STATE_START, deterministic=DETERMINISTIC):
        self.board = numpy.zeros([BOARD_WIDTH, BOARD_LENGTH])
        self.state = state
        self.endGame = False
        self.deterministic = DETERMINISTIC

    def valueReward(self):
        if self.state == STATE_WIN:
            self.endGame = True
            return 1
        elif self.state == STATE_LOSE:
            self.endGame= True
            return -1
        else:
            return 0

    def nextPosition(self, action):
        nextState = (0, 0)
        if self.deterministic:
            if action == "up":
                nextState = (self.state[0] - 1, self.state[1])
            if action == "down":
                nextState = (self.state[0] + 1, self.state[1])
            if action == "left":
                nextState = (self.state[0], self.state[1] - 1)
            if action == 'right':
                nextState = (self.state[0], self.state[1] + 1)
            if action == 'up-right':
                nextState = (self.state[0] - 1, self.state[1] + 1)
            if action == 'up-left':
                nextState = (self.state[0] - 1, self.state[1] - 1)
            if action == 'down-right':
                nextState = (self.state[0] + 1, self.state[1] + 1)
            if action == 'down-left':
                nextState = (self.state[0] + 1, self.state[1] - 1)
        if (nextState[0] >= 0) and (
            nextState[0] <= (BOARD_WIDTH - 1)) and (
            nextState[1] >= 0) and (
            nextState[1] <= (BOARD_LENGTH - 1)) and (
            nextState not in  STATE_OBSTACLES):
            return nextState
        return self.state

    def plotBoard(self):
        self.board[self.state] = 0.1
        self.board[STATE_WIN] = 1
        self.board[STATE_LOSE] = -1
        for i in STATE_OBSTACLES:
            self.board[i] = -0.1
        for i in range(BOARD_WIDTH):
            print('----' * BOARD_LENGTH + '-')
            out = '| '
            for j in range(BOARD_LENGTH):
                if self.board[i, j] == 0.1:
                    token = 'O'
                if self.board[i, j] == 1:
                    token = 'W'
                if self.board[i, j] == -1:
                    token = 'L'
                if self.board[i, j] == -0.1:
                    token = 'X'
                if self.board[i, j] == 0:
                    token = ' '
                out += token + ' | '
            print(out)
        print('----' * BOARD_LENGTH + '-')