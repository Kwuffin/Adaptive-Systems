from Maze import Maze
from Policy import Policy
import numpy as np


class Agent:
    def __init__(self, maze, policy, start_pos):
        self.maze = maze
        self.pos = start_pos
        self.policy = policy

        self.previous_values = np.zeros((4, 4))

        self.iteration = 0

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

    def value_iteration(self):
        while True:
            self.iteration += 1
            for x in self.maze.loc:
                for state in x:
                    if state in self.maze.terminate:
                        continue
                    coords = list(zip(*np.where(self.maze.loc == state)))[0]
                    state_values = []
                    states_to_calc = []
                    for action in range(4):
                        neigh_state = self.maze.step([[coords[0], coords[1]],
                                                     self.maze.rew[coords[0], coords[1]],
                                                     False],
                                                    action)

                        neigh_coords = neigh_state[0]
                        neigh_reward = self.maze.rew[neigh_coords[0], neigh_coords[1]]
                        neigh_old_value = self.previous_values[neigh_coords[0], neigh_coords[1]]

                        state_values.append(neigh_reward + 1 * neigh_old_value)  # Bellman equation

                    self.previous_values[coords[0], coords[1]] = max(state_values)
