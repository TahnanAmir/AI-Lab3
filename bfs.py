from collections import deque

def find_shortest_path(matrix):
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize starting and ending positions
    start = (1, 1)
    end = (4, 4)

    # Initialize data structures for BFS
    queue = deque([[start]])
    visited = set([start])

    # BFS Loop
    while queue:
        # Dequeue the next position
        path = queue.popleft()
        current_position = path[-1]

        # Check if HOME is reached
        if current_position == end:
            return path
        
        # Explore neighboring cells (non-diagonal and not obstacles)
        for direction in directions:
            new_position = (current_position[0] + direction[0], current_position[1] + direction[1])
            if (0 <= new_position[0] < len(matrix) and 
                0 <= new_position[1] < len(matrix[0]) and
                new_position not in visited and matrix[new_position[0]][new_position[1]] != 1):
                new_path = list(path)
                new_path.append(new_position)
                queue.append(new_path)
                visited.add(new_position)

    #Return the shortest path If found, else indicate no path
    return None

# incase of obstacles, write 1
matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

path = find_shortest_path(matrix)
if path:
    print("Shortest path:", path)
else:
    print("No path found")