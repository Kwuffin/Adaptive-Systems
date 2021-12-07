import numpy as np
from policies import *


class Agent:
    def __init__(self, maze, discount):
        self.maze = maze
        self.start = 2
        self.discount = discount

    def create_episode(self, maze, start_pos, terminal_states, policy):
        episode = [start_pos]
        state = start_pos
        while state not in terminal_states:
            state = policy(maze, state)
            episode.append(state)

        return episode

    def monte_carlo(self, iterations, policy):
        value_matrix = np.zeros((4, 4))
        returns = {}

        for iteration in range(iterations):

            # Generate a random start position
            rand_start = self.maze.terminate[0]
            while rand_start in self.maze.terminate:
                rand_start = np.random.randint(self.maze.loc.min(), self.maze.loc.max())

            episode = self.create_episode(self.maze, rand_start, self.maze.terminate, policy)  # Generate episode
            g = 0

            for i, step in reversed(list(enumerate(episode[-2::-1]))):
                coord = list(zip(*np.where(self.maze.loc == episode[i+1])))[0]
                reward = self.maze.rew[coord[0], coord[1]]
                g = self.discount * g + reward
                if step not in returns.keys():
                    returns[step] = [g]
                else:
                    returns[step].append(g)

        for state, state_returns in returns.items():
            state_coords = list(zip(*np.where(self.maze.loc == state)))[0]
            value_matrix[state_coords[0], state_coords[1]] = np.average(state_returns)

        print(f"{value_matrix}\n\n"
              f"Stats:\n"
              f"Iterations:    {iterations}\n"
              f"Discount rate: {self.discount}")

    def temporal_difference(self, policy, alpha=0.1):
        value_matrix = np.zeros((4, 4))
        episode = self.create_episode(self.maze, self.start, self.maze.terminate, policy)
        for step in episode:
            coord = list(zip(*np.where(self.maze.loc == step)))[0]
            reward = self.maze.rew[coord[0], coord[1]]

