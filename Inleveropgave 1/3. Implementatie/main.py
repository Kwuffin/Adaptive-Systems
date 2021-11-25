import numpy as np
from Agent import Agent
from Maze import Maze
from Policy import Policy

maze = Maze()
policy = Policy()
# agent = Agent(maze, policy, [np.random.randint(0, 3), np.random.randint(0, 3)])
agent = Agent(maze, policy, [3, 2])

agent.value_iteration()
