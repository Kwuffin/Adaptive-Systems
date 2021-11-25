import numpy as np


class Maze:
    def __init__(self):
        self.loc = np.array([[12, 13, 14, 15],
                            [8, 9, 10, 11],
                            [4, 5, 6, 7],
                            [0, 1, 2, 3]])
        self.rew = np.array([[-1, 1, -1, 40],
                            [-1, -1, -10, -10],
                            [-1, -1, -1, -1],
                            [10, -2, -1, -1]])
        self.act = [0, 1, 2, 3]  # [up, right, down, left]

    def step(self, current_state, action):
        """
        Given a state and action, performs the action and returns the next state
        :param current_state: State that agent is currently in
        :param action: Action that is te be performed
        :return: Next state after action is done.
        """

        # current_state should look like this:
        # [pos: [int, int], reward: int/float, finished: bool]
        coord, rew, fin = current_state
        pos = self.loc[coord[0], coord[1]]

        if action == 0:  # Up
            if pos in self.loc[0]:
                return current_state
            else:
                return [[coord[0] - 1, coord[1]],
                        self.rew[coord[0] - 1, coord[1]],
                        False]

        elif action == 1:  # Right
            if pos in self.loc[:, 3]:
                return current_state
            else:
                return [[coord[0], coord[1] + 1],
                        self.rew[coord[0], coord[1] + 1],
                        False]

        elif action == 2:  # Down
            if pos in self.loc[3]:
                return current_state
            else:
                return [[coord[0] + 1, coord[1]],
                        self.rew[coord[0] + 1, coord[1]],
                        False]

        elif action == 3:  # Left
            if pos in self.loc[:, 0]:
                return current_state
            else:
                return [[coord[0], coord[1] - 1],
                        self.rew[coord[0], coord[1] - 1],
                        False]

        else:
            Exception(f"Action not possible, `action` must be an integer between 0-3, not {action}")
