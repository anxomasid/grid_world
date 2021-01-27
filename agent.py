''' Agent '''

# import libraries, variables and classes
import numpy
from game_parameters import *
from state import State

# define Agent class
class Agent:
    def __init_(self, exporation_rate=EXPLORATION_RATE, learning_rate=LEARNING_RATE):
        self.State = State()
        self.states = []
        self.actions = ['up', 'down', 'right', 'left', 'up-right', 'up-left', 'down-right', 'down-left']
        self.learning_rate = learning_rate
        self.exploration_rate = exploration_rate
        self.state_reward_values = {}

        for i in range(BOARD_LENGTH):
            for j in range(BOARD_WIDTH):
                self.state_reward_values[(i, j)] = 0

    def chooseAction(self):

        action = ''
        next_reward = 0
        max_next_reward = 0

        if numpy.random.uniform(0, 1) <= self.exploration_rate:
            action = numpy.random.choice(self.actions)
        else:
            for i in self.actions:
                next_reward = self.state_reward_values[self.nextPosition(i)]
                if next_reward >= max_next_reward:
                    action = i
                    max_next_reward = next_reward

    def takeAction(self, action):
        position = self.State.nextPosition(action)
        return State(state=position)

    def reset(self):
        self.states = []
        self.State = State()

    def play(self, number_rounds=NUMBER_ROUNDS):
        'Falta'

    def showRewardValues(self):
        'Falta'
