import random

import numpy as np


def get_state(maze, state, action):
    state_coord = list(zip(*np.where(maze.loc == state)))[0]
    # Up
    if action == 0:
        if state in maze.loc[0]:
            return (state, action)
        else:
            # Update current state
            state = maze.loc[state_coord[0] - 1, state_coord[1]]
            return (state, action)

    # Right
    elif action == 1:
        if state in maze.loc[:, -1]:
            return (state, action)
        else:
            # Update current state
            state = maze.loc[state_coord[0], state_coord[1] + 1]
            return (state, action)

    # Down
    elif action == 2:
        if state in maze.loc[-1]:
            return (state, action)
        else:
            # Update current state
            state = maze.loc[state_coord[0] + 1, state_coord[1]]
            return (state, action)

    # Left
    else:
        if state in maze.loc[:, 0]:
            return (state, action)
        else:
            # Update current state
            state = maze.loc[state_coord[0], state_coord[1] - 1]
            return (state, action)


def random_policy(maze, state):
    # Get a random action
    action = np.random.randint(0, 4)  # 0: Up, 1: Right, 2: Down, 3: Left
    return get_state(maze, state, action)


def optimal_policy(maze, state):
    policy_matrix = np.array([[1, 1, 1, 9],
                              [0, 0, 0, 0],
                              [0, 0, 3, 3],
                              [9, 0, 0, 0]])

    coords = list(zip(*np.where(maze.loc == state)))[0]
    action = policy_matrix[coords[0], coords[1]]
    if action != 9:  # 9-Dimensional movement is not possible
        return get_state(maze, state, action)


def epsilon_soft_policy(maze, state, epsilon):
    policy_matrix = np.array([[1, 1, 1, 9],
                              [0, 0, 0, 0],
                              [0, 0, 3, 3],
                              [9, 0, 0, 0]])

    coords = list(zip(*np.where(maze.loc == state)))[0]
    chance = (1-((epsilon/4)*3))*1000000
    best_action = policy_matrix[coords[0], coords[1]]
    if np.random.randint(0, 1000000) < chance:
        action = policy_matrix[coords[0], coords[1]]
        return get_state(maze, state, action)

    else:
        rand_act_non_optimal = best_action
        while rand_act_non_optimal == best_action:
            rand_act_non_optimal = np.random.rand(0, 3)
        return get_state(maze, state, rand_act_non_optimal)

