# Rupesh Dharme 
# TE 01 31124
# L1 
# Assignment 02
# Implement A* search algorithm in any game search problem.


# Representing the board as a matrix, plant means cat can walk, box means cat cannot walk.
board = [['🌾', '🌾', '📦', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾'],
         ['🌾', '📦', '📦', '🌾', '📦', '🌾', '📦', '📦', '📦'],
         ['🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '📦'],
         ['🌾', '🌾', '🌾', '🌾', '📦', '🌾', '🌾', '🌾', '🌾'],
         ['🌾', '📦', '🌾', '🌾', '📦', '🌾', '📦', '📦', '🌾'],
         ['🌾', '📦', '🌾', '📦', '📦', '🌾', '🌾', '📦', '🌾'],
         ['📦', '📦', '🌾', '🌾', '📦', '🌾', '🌾', '📦', '🌾'],
         ['🌾', '🌾', '🌾', '🌾', '📦', '🌾', '🌾', '📦', '🌾'],
         ['🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾']]

# Heuristic function which returns the euclidean distance.
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

# Implementation of A* Algorithm.
def play():
    while True:  # Exits when g(Number of steps) is returned.
        open_list.sort()
        # Choosing element with least f value, followed by least h value.
        f, h, g, x, y = open_list.pop(0)

        if x == x2 and y == y2:  # Destination reached!
            return g

        closed_list.append((x, y))  # Adding current position to closed list.
        board[x][y] = '❌'  # Marking the path as tried.

        # Going >
        if x+1 < len(board) and (x+1, y) not in closed_list and board[x+1][y] != '📦':
            # Marking current position as parent of right cell.
            parents[x+1][y] = (x, y)
            h = heuristic((x+1, y), (x2, y2))
            # Adding right cell to open list.
            open_list.append([g + h + 1, h, g+1, x+1, y])

        # Going <
        if x-1 >= 0 and (x-1, y) not in closed_list and board[x-1][y] != '📦':
            parents[x-1][y] = (x, y)
            h = heuristic((x-1, y), (x2, y2))
            open_list.append([g + h + 1, h, g+1, x-1, y])

        # Going ↓
        if y+1 < len(board[0]) and (x, y+1) not in closed_list and board[x][y+1] != '📦':
            parents[x][y+1] = (x, y)
            h = heuristic((x, y+1), (x2, y2))
            open_list.append([g + h + 1, h, g+1, x, y+1])

        # Goint ^
        if y-1 >= 0 and (x, y-1) not in closed_list and board[x][y-1] != '📦':
            parents[x][y-1] = (x, y)
            h = heuristic((x, y-1), (x2, y2))
            open_list.append([g + h + 1, h, g+1, x, y-1])

# As we now have the parents of each travelled cell, we can start from destination and find the Path.
def show_path(ex, ey):
    while ex != x1 or ey != y1:  # While current is not the starting point.
        board[ex][ey] = '⭐'
        ex, ey = parents[ex][ey]  # Current position -> parent position.
    board[x2][y2] = '🥛'
    # Mark starting point as a cat and Destination as Milk.
    board[x1][y1] = '🐈'
    print_board()

# Printing the Board.
def print_board():
    for row in board:
        for element in row:
            print(element, end='  ')
        print()
        print()


if __name__ == '__main__':
    # Input starting and destination coordinates.
    x1, y1 = map(int, input("Enter the starting point: ").split())
    x2, y2 = map(int, input("Enter the ending point: ").split())

    # Marking starting and destination coordinates.
    board[x2][y2] = '🥛'
    board[x1][y1] = '🐈'
    print_board()

    # Creating open list with the starting cell and an empty closed list.
    h = heuristic((x1, y1), (x2, y2))
    g = 0
    path = []
    # Each element is in [f, h, g, x, y] format.
    open_list = [[h + g, h, g, x1, y1]]
    closed_list = []  # Each element is in (X, Y) format.

    # Creating parents matrix to track path.
    parents = [[(-1, -1) for j in range(len(board[0]))]
               for i in range(len(board))]

    # Execution of A* Algorithm.
    print(f"\nThe cat will reach it's destination in {play()} moves.\n")
    print("\nThe path taken by the cat is:")
    ex, ey = x2, y2
    show_path(ex, ey)
