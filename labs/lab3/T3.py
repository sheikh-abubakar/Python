import heapq

# ---------------- Priority Queue ----------------
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def enqueue(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def dequeue(self):
        return heapq.heappop(self.elements)[1]
    
    def is_empty(self):
        return len(self.elements) == 0


# ---------------- Node Class ----------------
class Node:
    goal_state = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]
    
    def __init__(self, state, parent=None, g=0):
        self.state = state
        self.parent = parent
        self.g = g                              # cost so far
        self.h = self.heuristic(state)          # estimated cost to goal
        self.f = self.g + self.h                # total cost

    def __lt__(self, other):                    # needed for heapq
        return self.f < other.f

    def heuristic(self, state):                 # Manhattan Distance
        distance = 0
        for i in range(3):
            for j in range(3):
                value = state[i][j]
                if value != 0:
                    goal_i, goal_j = divmod(value - 1, 3)
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance


# ---------------- Puzzle Solver ----------------
class PuzzleSolver:
    def __init__(self, start):
        self.start = start
        self.goal = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 0]]

    def find_space(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)

    def find_moves(self, pos):
        i, j = pos
        moves = []
        if i > 0: moves.append((-1, 0))  # Up
        if i < 2: moves.append((1, 0))   # Down
        if j > 0: moves.append((0, -1))  # Left
        if j < 2: moves.append((0, 1))   # Right
        return moves

    def play_move(self, state, move, space):
        i, j = space
        di, dj = move
        new_state = [row[:] for row in state]
        new_i, new_j = i + di, j + dj
        new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
        return new_state

    def find_children(self, state):
        space = self.find_space(state)
        moves = self.find_moves(space)
        children = []
        for move in moves:
            new_state = self.play_move(state, move, space)
            children.append(new_state)
        return children

    def solve_puzzle(self):
        pq = PriorityQueue()
        start_node = Node(self.start)
        pq.enqueue(start_node, start_node.f)
        explored = set()

        while not pq.is_empty():
            current = pq.dequeue()
            explored.add(tuple(map(tuple, current.state)))

            if current.state == self.goal:
                return self.print_solution(current)

            for child_state in self.find_children(current.state):
                if tuple(map(tuple, child_state)) not in explored:
                    child_node = Node(child_state, current, current.g + 1)
                    pq.enqueue(child_node, child_node.f)
        
        return None

    def print_solution(self, node):
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        path.reverse()
        return path


# ---------------- Run the Solver ----------------
if __name__ == "__main__":
    ps = PuzzleSolver([[4, 7, 8],
                       [3, 6, 5],
                       [1, 2, 0]])

    solution = ps.solve_puzzle()
    if solution:
        print("Solution found in", len(solution)-1, "moves:\n")
        for state in solution:
            for row in state:
                print(row)
            print()
    else:
        print("No solution found.")
