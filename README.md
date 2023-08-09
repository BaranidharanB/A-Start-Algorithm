# A-Start- Path Finding Algorithm

- The A* algorithm is a popular search algorithm used in pathfinding and graph traversal. It works by finding the lowest-cost path between a start node and a goal node in a graph, where each node represents a location and the edges represent the possible paths between them.
- It's an effective algorithm for pathfinding and graph traversal. By using the heuristic function h(n) to estimate the cost of reaching the goal, A* can search the graph more efficiently than other search algorithms.
  
- A* algorithm Working

1. Initialization: The algorithm starts by initializing the start and endpoints. The start point is the current position of the Robot, and the endpoint is the desired destination.
2. Evaluation: The algorithm creates a list of open nodes, which includes the start point. The algorithm then evaluates each node in the list based on its cost and the estimated distance to the goal. The algorithm selects the node with the lowest combined cost and distance and moves it from the open list to the closed list.
3. Expansion: The algorithm expands the selected node by examining its neighboring nodes. For each neighboring node, the algorithm calculates the cost to move to that node from the current node and the estimated distance to the goal. The algorithm then adds the neighboring node to the open list.
4. Selection: The algorithm selects the next node from the open list with the lowest combined cost and distance. The algorithm then repeats steps 3 and 4 until the goal is reached or there are no more nodes left in the open list.
5. Path: Once the algorithm reaches the goal, it traces back the path from the goal to the start node by following the parents of each node. The resulting path is the optimal path from the start node to the goal node.


# A* Working Video: 

https://github.com/BaranidharanB/A-Start-Algorithm/assets/118863352/7d0dde7a-4e20-45d6-8d9a-707ec28f7469
