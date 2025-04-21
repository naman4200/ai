# goal = "123456789"

# def is_solvable(state):
#     inv_count = 0
#     for i in range(9):
#         for j in range(i + 1, 9):
#             # Check for inversions, excluding the empty tile ('0')
#             if state[i] != '0' and state[j] != '0' and state[i] > state[j]:
#                 inv_count += 1
#     # Puzzle is solvable if inversions count is even
#     return inv_count % 2 == 0

# state = "281043765"
# print("Solvable:", is_solvable(state))



# code 2


goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

class Puzzle:
    def __init__(self, state, parent=None, move=0):
        self.state = state
        self.parent = parent
        self.move = move

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_children(self):
        x, y = self.find_zero()
        children = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in self.state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                children.append(Puzzle(new_state, self, self.move + 1))
        return children

    def is_goal(self):
        return self.state == goal_state

    def print_path(self):
        path = []
        node = self
        while node:
            path.append(node.state)
            node = node.parent
        path.reverse()
        for step in path:
            for row in step:
                print(row)
            print()

def solve(start_state):
    start = Puzzle(start_state)
    open_set = [start]
    visited = set()

    while open_set:
        current = open_set.pop(0)  # Pop from front for BFS
        if current.is_goal():
            print("Solved in", current.move, "moves!")
            current.print_path()
            return

        visited.add(str(current.state))

        for child in current.generate_children():
            if str(child.state) not in visited:
                open_set.append(child)

# Example start state
start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

solve(start)
