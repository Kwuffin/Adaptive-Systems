from Maze import Maze
from Agent import Agent
from policies import random_policy, optimal_policy

maze = Maze()
agent = Agent(maze, 1)
agent_discounted = Agent(maze, 0.9)

# agent.monte_carlo(1000, optimal_policy)
agent.temporal_difference(optimal_policy)
agent_discounted.temporal_difference(optimal_policy)
