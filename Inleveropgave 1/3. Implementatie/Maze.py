import numpy as np


class Maze:
    def __init__(self):
        self.loc = np.array([[12, 13, 14, 15],
                            [8, 9, 10, 11],
                            [4, 5, 6, 7],
                            [0, 1, 2, 3]])
        self.rew = np.array([[-1, 1, -1, 0],
                            [-1, -1, -1, -1],
                            [-1, -1, -1, -1],
                            [0, -1, -1, -1]])
        self.act = [0, 1, 2, 3]  # [up, right, down, left]

    def step(self, current_state, action):
        # current_state should look like this:
        # [pos, reward: int/float, finished: bool]
        coord, rew, fin = current_state
        pos = self.loc[coord[0], coord[1]]

        if action == 0:
            if pos in self.loc[0]:
                return current_state
            else:
                return [[coord[0] - 1, coord[1]],
                        self.rew[coord[0] - 1, coord[1]],
                        False]

        elif action == 1:
            if pos in self.loc[:, 3]:
                return current_state
            else:
                return [[coord[0], coord[1] + 1],
                        self.rew[coord[0], coord[1] + 1],
                        False]

        elif action == 2:
            if pos in self.loc[3]:
                return current_state
            else:
                return [[coord[0] + 1, coord[1]],
                        self.rew[coord[0] + 1, coord[1]],
                        False]
        elif action == 3:
            if pos in self.loc[:, 0]:
                return current_state
            else:
                return [[coord[0], coord[1] - 1],
                        self.rew[coord[0], coord[1] - 1],
                        False]
        else:
            Exception(f"Action not possible, `action` must be an integer between 0-3, not {action}")
