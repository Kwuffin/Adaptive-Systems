from Maze import Maze
from Agent import Agent

maze = Maze()
agent = Agent(maze)

print(agent.create_episode(maze, agent.start, maze.terminate))
