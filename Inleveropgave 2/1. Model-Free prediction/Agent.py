import numpy as np


class Agent:
    def __init__(self, maze, discount):
        self.maze = maze
        self.start = 2
        self.discount = discount

    def create_episode(self, maze, start_pos, terminal_states):
        episode = [start_pos]
        state = start_pos
        state_coord = list(zip(*np.where(maze.loc == start_pos)))[0]
        while state not in terminal_states:
            # Get a random neighbor
            neigh = np.random.randint(0, 4)  # 0: Up, 1: Right, 2: Down, 3: Left

            # Up
            if neigh == 0:
                if state in maze.loc[0]:
                    episode.append(state)
                else:
                    # Update current state
                    state = maze.loc[state_coord[0] - 1, state_coord[1]]
                    state_coord = list(zip(*np.where(maze.loc == state)))[0]
                    episode.append(state)

            # Right
            elif neigh == 1:
                if state in maze.loc[:,-1]:
                    episode.append(state)
                else:
                    # Update current state
                    state = maze.loc[state_coord[0], state_coord[1] + 1]
                    state_coord = list(zip(*np.where(maze.loc == state)))[0]
                    episode.append(state)

            # Down
            elif neigh == 2:
                if state in maze.loc[-1]:
                    episode.append(state)
                else:
                    # Update current state
                    state = maze.loc[state_coord[0] + 1, state_coord[1]]
                    state_coord = list(zip(*np.where(maze.loc == state)))[0]
                    episode.append(state)

            else:
                if state in maze.loc[:,0]:
                    episode.append(state)
                else:
                    # Update current state
                    state = maze.loc[state_coord[0], state_coord[1] - 1]
                    state_coord = list(zip(*np.where(maze.loc == state)))[0]
                    episode.append(state)

        return episode

    def monte_carlo(self, iterations):
        value_matrix = np.zeros((4, 4))
        returns = {}

        for iteration in range(iterations):
            episode = self.create_episode(self.maze, self.start, self.maze.terminate)  # Generate episode
            g = 0

            for step in episode[-2::-1]:
                coord = list(zip(*np.where(self.maze.loc == step)))[0]
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

    def temporal_difference_learning(self):
        pass
