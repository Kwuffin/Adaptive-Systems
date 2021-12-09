import numpy as np


class Maze:
    def __init__(self):
        self.loc = np.array([[12, 13, 14, 15],
                             [8, 9, 10, 11],
                             [4, 5, 6, 7],
                             [0, 1, 2, 3]])
        self.rew = np.array([[-1, -1, -1, 40],
                             [-1, -1, -10, -10],
                             [-1, -1, -1, -1],
                             [10, -2, -1, -1]])
        self.act = [0, 1, 2, 3]  # [up, right, down, left]
        self.terminate = [0, 15]
