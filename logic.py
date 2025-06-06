import random


def start_game():
    mat = [[0] * 4 for _ in range(4)]
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    add_new_2(mat)
    return mat


def add_new_2(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if not empty_cells:
        return
    r, c = random.choice(empty_cells)
    mat[r][c] = 2


def get_current_state(mat):
    for row in mat:
        if 2048 in row:
            return "WON"
    for row in mat:
        if 0 in row:
            return "GAME NOT OVER"
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] or mat[j][i] == mat[j + 1][i]:
                return "GAME NOT OVER"
    return "LOST"


def compress(mat):
    new_mat = [[0] * 4 for _ in range(4)]
    changed = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed


def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed


def reverse(mat):
    return [row[::-1] for row in mat]


def transpose(mat):
    return [list(row) for row in zip(*mat)]


def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    new_grid, _ = compress(new_grid)
    return new_grid, changed1 or changed2


def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed


def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed


def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed


def calculate_score(mat):
    return sum(sum(row) for row in mat)
