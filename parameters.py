''' Game Parameters '''

# board dimensions
BOARD_LENGTH = 5
BOARD_WIDTH = 5

# game key states
STATE_START = (1, 1)
STATE_WIN = (2, 3)
STATE_LOSE = (3, 2)
STATE_OBSTACLES = [(1, 3), (3, 1)]

# options
DETERMINISTIC = True
EXPLORATION_RATE = 0.3
LEARNING_RATE = 0.3
NUMBER_ROUNDS = 10