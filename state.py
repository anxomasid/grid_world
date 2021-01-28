''' State '''

import numpy
from parameters import *

class State:

    def __init__(self, state=STATE_START, deterministic=DETERMINISTIC):
        self.board = numpy.zeros(BOARD_LENGTH, BOARD_WIDTH)
        self.state = state
        self.endGame = False
        self.deterministic = DETERMINISTIC

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
        if self.deterministic:
            if action == 'up':
                nextState = (self.state[0], self.state[1] + 1)
            elif action == 'down':
                nextState = (self.state[0], self.state[1] - 1)
            elif action == 'right':
                nextState = (self.state[0] + 1, self.state[1])
            elif action == 'left':
                nextState = (self.state[0] - 1, self.state[1])
            elif action == 'up-right':
                nextState = (self.state[0] + 1, self.state[1] + 1)
            elif action == 'up-left':
                nextState = (self.state[0] + 1, self.state[1] - 1)
            elif action == 'down-right':
                nextState = (self.state[0] + 1, self.state[1] - 1)
            elif action == 'down-left':
                nextState = (self.state[0] - 1, self.state[1] - 1)
            if (nextState[0] >= 1) and (
                nextState[0] <= (BOARD_LENGTH)) and (
                nextState[1] >= 1) and (
                nextState[1] <= (BOARD_WIDTH)) and (
                nextState not in STATE_OBSTACLES):
                return nextState
        return self.state

    def plotBoard(self):
        self.board[self.state] = 0.1
        self.board[WIN_STATE] = 1
        self.board[LOSE_STATE] = -1
        self.board[(1, 1)] = -0.1
        for i in range(1, BOARD_WIDTH + 1):
            print('----' * BOARD_LENGTH + '-')
            out = '| '
            for j in range(0, BOARD_LENGTH):
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
        print('----' * BOARD_BOARD_LENGTH + '-')