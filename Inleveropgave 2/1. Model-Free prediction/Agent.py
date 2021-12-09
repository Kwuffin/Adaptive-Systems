import numpy as np
from policies import *


class Agent:
    def __init__(self, maze, discount):
        self.maze = maze
        self.start = 2
        self.discount = discount

    def create_episode(self, maze, start_pos, terminal_states, policy, epsilon=0):
        episode = [(start_pos, 9)]
        state = start_pos
        while state not in terminal_states:
            state_act = policy(maze, state, epsilon)
            episode.append(state_act)
            state = state_act[0]

        return episode

    def monte_carlo(self, iterations, policy):
        value_matrix = np.zeros((4, 4))
        returns = {}

        for iteration in range(iterations):

            # Generate a random start position
            rand_start = self.maze.terminate[0]
            while rand_start in self.maze.terminate:
                rand_start = np.random.randint(self.maze.loc.min(), self.maze.loc.max())

            episode, ep_act = zip(*self.create_episode(self.maze, rand_start, self.maze.terminate, policy))  # Generate episode
            g = 0

            frequency_table = {}
            for step in episode:
                if step in frequency_table:
                    frequency_table[step] += 1
                else:
                    frequency_table[step] = 1

            count_table = {}
            for i, step in reversed(list(enumerate(episode[-2::-1]))):
                coord = list(zip(*np.where(self.maze.loc == episode[i + 1])))[0]
                reward = self.maze.rew[coord[0], coord[1]]
                g = self.discount * g + reward

                # Check first-visit:
                if step in count_table:
                    count_table[step] += 1
                else:
                    count_table[step] = 1

                # If first-visit == True:
                if count_table[step] == frequency_table[step]:
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

    def temporal_difference(self, iterations, policy, alpha=0.1, exploring_start=True):
        value_matrix = np.zeros((4, 4))
        for _ in range(iterations):
            if exploring_start:
                start_pos = np.random.randint(self.maze.loc.min(), self.maze.loc.max())
            else:
                start_pos = self.start
            episode, ep_act = zip(*self.create_episode(self.maze, start_pos, self.maze.terminate, policy))
            for i, step in enumerate(episode[:-1:]):
                coord = list(zip(*np.where(self.maze.loc == step)))[0]
                next_coord = list(zip(*np.where(self.maze.loc == episode[i + 1])))[0]
                reward = self.maze.rew[next_coord[0], next_coord[1]]
                value_matrix[coord[0], coord[1]] = value_matrix[coord[0], coord[1]] + alpha * \
                                                   (reward + self.discount * value_matrix[next_coord[0], next_coord[1]] -
                                                    value_matrix[coord[0], coord[1]])

        print(f"{value_matrix}\n\n"
              f"Stats:\n"
              f"Iterations:      {iterations}\n"
              f"Discount rate:   {self.discount}\n"
              f"Alpha:           {alpha}\n"
              f"Exploring Start: {exploring_start}")

    def on_policy_monte_carlo(self, iterations, epsilon, policy):
        q_matrix = np.full((4, 4), {0: [], 1: [], 2: [], 3: []})
        returns = {}

        for _ in range(iterations):
            episode, ep_act = zip(*self.create_episode(self.maze, self.start, self.maze.terminate, policy, epsilon))
            g = 0

            frequency_table = {}
            for step, action in zip(episode, ep_act):
                if step not in frequency_table:
                    frequency_table[step] = {action: 1}
                elif action not in frequency_table[step]:
                    frequency_table[step][action] = 1
                else:
                    frequency_table[step][action] += 1

            count_table = {}
            for i, (step, action) in reversed(list(enumerate(zip(episode[-2::-1], ep_act[-2::-1])))):
                coord = list(zip(*np.where(self.maze.loc == episode[i + 1])))[0]
                reward = self.maze.rew[coord[0], coord[1]]
                g = self.discount * g + reward

                if step not in count_table:
                    count_table[step] = {action: 1}
                elif action not in count_table[step]:
                    count_table[step][action] = 1
                else:
                    count_table[step][action] += 1

                if count_table[step][action] == frequency_table[step][action]:
                    if step not in returns.keys():
                        returns[step] = {action: [g]}
                    elif action not in returns[step].keys():
                        returns[step][action] = [g]
                    else:
                        returns[step][action].append(g)

        for state, act_values in returns.items():
            coord = list(zip(*np.where(self.maze.loc == state)))[0]
            for act, values in act_values.items():
                if act == 9:
                    continue
                avg_val = np.average(values)
                q_matrix[coord[0], coord[1]][act] = avg_val

        print(f"Actions:\n0 = Up | 1 = Right | 2 = Down | 3 = Left\n")
        state_nr = -1
        for row in q_matrix:
            for state in row:
                state_nr += 1
                print(f"State: {state_nr}\n",
                      f"Action:   |    Value:")
                for action, value in state.items():
                    print(f"{action}          |    {value}")
