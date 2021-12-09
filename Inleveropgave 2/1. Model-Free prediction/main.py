from Maze import Maze
from Agent import Agent
from policies import random_policy, optimal_policy

maze = Maze()
agent = Agent(maze, 1)
agent_discounted = Agent(maze, 0.9)

iterations = 1000

print("First-Visit Monte Carlo:")
print("Random policy:")
agent.monte_carlo(iterations, random_policy)
print("-----------------")
agent_discounted.monte_carlo(iterations, random_policy)
print("===========================================\n")

print("Optimal policy:")
agent.monte_carlo(iterations, optimal_policy)
print("-----------------")
agent_discounted.monte_carlo(iterations, optimal_policy)
print("===========================================\n")


print("Temporal Difference:")
print("Random policy:")
agent.temporal_difference(iterations, random_policy)
print("-----------------")
agent_discounted.temporal_difference(iterations, random_policy)
print("===========================================\n")

print("Optimal policy:")
agent.temporal_difference(iterations, optimal_policy)
print("-----------------")
agent_discounted.temporal_difference(iterations, optimal_policy)
print("===========================================\n")
