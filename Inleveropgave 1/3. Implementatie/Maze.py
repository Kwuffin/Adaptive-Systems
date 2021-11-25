import numpy as np


class Maze:
    def __init__(self):
        loc = np.arange([12, 13, 14, 15],
                        [8, 9, 10, 11],
                        [4, 5, 6, 7],
                        [0, 1, 2, 3])
        rew = np.arange([-1, 1, -1, 0],
                        [-1, -1, -1, -1],
                        [-1, -1, -1, -1],
                        [0, -1, -1, -1])
        act = [0, 1, 2, 3]  # [up, right, down, left]

    def step(self, current_state, action):
        # current_state should look like this:
        # [pos, reward: int/float, finished: bool]
        pass
