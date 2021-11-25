from Maze import Maze
from Policy import Policy
import numpy as np


class Agent:
    def __init__(self, maze, policy, start_pos):
        self.maze = maze
        self.pos = start_pos
        self.policy = policy

    def value_func(self, current_state):
        # values = np.zeros((4, 4))
        # coords = current_state[0]
        # pos = self.maze.loc[coords[0], coords[1]]
        # adjacent_states = [self.maze.loc[coords[0] + 1, coords[1]],
        #                    self.maze.loc[coords[0] - 1, coords[1]],
        #                    self.maze.loc[coords[0], coords[1] + 1],
        #                    self.maze.loc[coords[0], coords[1] - 1]]
        # adjacent_rewards = [self.maze.rew[coords[0] + 1, coords[1]],
        #                     self.maze.rew[coords[0] - 1, coords[1]],
        #                     self.maze.rew[coords[0], coords[1] + 1],
        #                     self.maze.rew[coords[0], coords[1] - 1]]
        # for reward in adjacent_rewards:
        #     0.25 * (reward + 1 * values[])
        pass

    def next_action(self, policy, state):
        pass

    def value_iteration(self):
        values = np.zeros((4, 4))

