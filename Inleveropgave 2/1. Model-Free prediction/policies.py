import numpy as np


def get_state(maze, state, action):
    state_coord = list(zip(*np.where(maze.loc == state)))[0]
    # Up
    if action == 0:
        if state in maze.loc[0]:
            return state
        else:
            # Update current state
            state = maze.loc[state_coord[0] - 1, state_coord[1]]
            state_coord = list(zip(*np.where(maze.loc == state)))[0]
            return state

    # Right
    elif action == 1:
        if state in maze.loc[:, -1]:
            return state
        else:
            # Update current state
            state = maze.loc[state_coord[0], state_coord[1] + 1]
            state_coord = list(zip(*np.where(maze.loc == state)))[0]
            return state

    # Down
    elif action == 2:
        if state in maze.loc[-1]:
            return state
        else:
            # Update current state
            state = maze.loc[state_coord[0] + 1, state_coord[1]]
            state_coord = list(zip(*np.where(maze.loc == state)))[0]
            return state

    else:
        if state in maze.loc[:, 0]:
            return state
        else:
            # Update current state
            state = maze.loc[state_coord[0], state_coord[1] - 1]
            state_coord = list(zip(*np.where(maze.loc == state)))[0]
            return state


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

