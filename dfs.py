import time

def state_to_tuple(state):
    """Convert a string state to a tuple representation."""
    return tuple(state)

def tuple_to_state(matrix):
    """Convert a tuple representation back to a string state."""
    return ''.join(matrix)

def get_moves(state):
    """Generate possible moves from the given state."""
    moves = []
    index = state.index('0')
    row, col = divmod(index, 3)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            moves.append(tuple(new_state))
    
    return moves

def dfs(start_state, goal_state):
    """Perform Depth-First Search (DFS) to find a solution path."""
    stack = [(start_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        path = path + [current_state]

        if current_state == goal_state:
            return path
        
        for move in get_moves(current_state):
            if move not in visited:
                stack.append((move, path))
    
    return None

def main():
    """Main function to take input and execute the DFS algorithm."""
    start_state = input("Enter start State: ")
    goal_state = input("Enter goal State: ")
    
    start_tuple = state_to_tuple(start_state)
    goal_tuple = state_to_tuple(goal_state)
    
    print("-----------------")
    print("DFS Algorithm")
    print("-----------------")
    
    start_time = time.time()
    solution_path = dfs(start_tuple, goal_tuple)
    end_time = time.time()
    
    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path) - 1)
        print("No of Nodes Visited:", len(solution_path))
        
        for state in solution_path:
            for i in range(0, 9, 3):
                print(' '.join(state[i:i+3]))
            print("------")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()