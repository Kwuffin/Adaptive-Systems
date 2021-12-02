import numpy as np


class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.start = 2

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

    def monte_carlo_policy(self):
        value_matrix = np.zeros((4, 4))
        returns = []

        for iteration in range(100):
            episodes = []  # Generate episode(s)
            for episode in episodes:
                pass
