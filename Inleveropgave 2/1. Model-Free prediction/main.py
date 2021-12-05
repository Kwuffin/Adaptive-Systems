from Maze import Maze
from Agent import Agent

maze = Maze()
agent = Agent(maze, 1)

agent.monte_carlo(iterations=1000)
