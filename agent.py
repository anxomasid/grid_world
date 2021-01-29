''' Agent '''

import numpy
from game_parameters import *
from state import State

class Agent:
    def __init__(self, exploration_rate=EXPLORATION_RATE, learning_rate=LEARNING_RATE):
        self.state = State()
        self.states = []
        self.actions = ['up', 'down', 'right', 'left', 'up-right', 'up-left', 'down-right', 'down-left']
        self.learning_rate = learning_rate
        self.exploration_rate = exploration_rate
        self.state_reward_values = {}
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_LENGTH):
                self.state_reward_values[(i, j)] = 0

    def chooseAction(self):
        action = ''
        next_reward = 0
        max_next_reward = 0
        if numpy.random.uniform(0, 1) <= self.exploration_rate:
            action = numpy.random.choice(self.actions)
        else:
            for i in self.actions:
                next_reward = self.state_reward_values[self.state.nextPosition(i)]
                if next_reward >= max_next_reward:
                    action = i
                    max_next_reward = next_reward
        return action

    def takeAction(self, action):
        position = self.state.nextPosition(action)
        return State(state=position)

    def reset(self):
        self.states = []
        self.state = State()

    def play(self, number_rounds=NUMBER_ROUNDS, graphics=False):
        self.graphics = graphics
        i = 1
        j = 0
        while i < number_rounds + 1:
            if self.state.endGame:
                reward = self.state.valueReward()
                self.state_reward_values[self.state.state] = reward
                print("Game {} End Reward {}: #movements {}".format(i, reward, j))
                for s in reversed(self.states):
                    reward = self.state_reward_values[s] + self.learning_rate * (reward - self.state_reward_values[s])
                    self.state_reward_values[s] = round(reward, 3)
                self.reset()
                i += 1
                j = 0
            else:
                action = self.chooseAction()
                self.states.append(self.state.nextPosition(action))
                self.state = self.takeAction(action)
                self.state.valueReward()
                if self.graphics:
                    self.state.plotBoard()
                j += 1

    def showRewardValues(self):
        for i in range(BOARD_WIDTH):
            print('---------' * BOARD_LENGTH + '-')
            out = '| '
            for j in range(BOARD_LENGTH):
                out += str(self.state_reward_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('---------' * BOARD_LENGTH + '-')