from Maze import Maze
import numpy as np


class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.start = 2

    def create_episode(self, maze, start_pos, terminal_states):
        episode = []
        state = start_pos
        state_coord = list(zip(*np.where(maze.loc == start_pos)))[0]
        while state not in terminal_states:

            pass

        return episode

    def monte_carlo_policy(self):
        value_matrix = np.zeros((4, 4))
        returns = []

        for iteration in range(100):
            episodes = []  # Generate episode(s)
            for episode in episodes:
                pass
