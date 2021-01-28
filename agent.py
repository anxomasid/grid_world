''' Agent '''

import numpy
from game_parameters import *
from state import State

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
        i = 0
        j = 0
        while i < rounds:
            # to the end of game back propagate reward
            if self.State.isEnd:
                # back propagate
                reward = self.State.giveReward()
                # explicitly assign end state to reward values
                self.state_values[self.State.state] = reward  # this is optional
                print("Game {} End Reward {}: #movements {}".format(i, reward, j))
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.lr * (reward - self.state_values[s])
                    self.state_values[s] = round(reward, 3)
                self.reset()
                i += 1
                j = 0
            else:
                action = self.chooseAction()
                # append trace
                self.states.append(self.State.nxtPosition(action))
                #print("current position {} action {}".format(self.State.state, action))
                # by taking the action, it reaches the next state
                self.State = self.takeAction(action)
                # mark is end
                self.State.isEndFunc()
                #print("nxt state", self.State.state)
                #print("---------------------")
                j += 1

    def showRewardValues(self):
        for i in range(1, BOARD_WIDTH):
            print('---------' * BOARD_LENGTH + '-')
            out = '| '
            for j in range(0, BOARD_LENGTH):
                out += str(self.state_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('---------' * BOARD_LENGTH + '-')
