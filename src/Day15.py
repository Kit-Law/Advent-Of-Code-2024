import Helpers.Grids as Grids


def gen_grid(filepath):
    grid = Grids.Grid()
    moves = []
    pos = (0, 0)

    is_reading_moves = False

    with open(filepath) as file:
        for y, line in enumerate(file):
            if line == "\n":
                is_reading_moves = True
                continue
            if is_reading_moves:
                moves += list(line.rstrip())
                continue
            try:
                starting_pos = line.index("@")
                pos = (y, starting_pos)
            except:
                pass

            grid.append(list(line.rstrip()))

    return (grid, moves, pos)


moves_map = {
    "^": "N",
    ">": "E",
    "v": "S",
    "<": "W",
}


def cal_gps_sum(grid):
    gps_sum = 0
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[(j, i)] == "O" or grid[(j, i)] == "[":
                gps_sum += 100 * j + i

    return gps_sum


def star_one(filepath):
    grid, moves, robot_pos = gen_grid(filepath)

    for move in moves:
        path = []
        pos_to_check = robot_pos
        while True:
            path.append(pos_to_check)
            pos_to_check = Grids.get_adjacent_points(pos_to_check)[moves_map[move]]
            
            if grid[pos_to_check] == ".":
                path.append(pos_to_check)
                grid[path[0]] = '.'
                grid[path[1]] = '@'
                robot_pos = path[1]
                if len(path) <= 2:
                    break
                for point in path[2:]:
                    grid[point] = "O"
                break
            if grid[pos_to_check] == "#":
                break

    return cal_gps_sum(grid)


def make_wide_grid(grid, pos):
    wide_grid = Grids.Grid()

    for row in grid:
        line = []
        for element in row:
            if element == "#":
                line += ["#", "#"]
            elif element == "O":
                line += ["[", "]"]
            elif element == ".":
                line += [".", "."]
            else:
                line += ["@", "."]
        wide_grid.append(line)

    return (wide_grid, (pos[0], pos[1] * 2))


def is_vertically_moveable(grid, pos, direction):
    if grid[pos] == ".":
        return True
    if grid[pos] == "#":
        return False
    
    next = Grids.get_adjacent_points(pos)[direction]
    if (grid[pos] == "[" or grid[pos] == "@") and grid[next] == "]":
        return (is_vertically_moveable(grid, next, direction) and
        is_vertically_moveable(grid, (next[0], next[1] - 1), direction))
    elif (grid[pos] == "]" or grid[pos] == "@") and grid[next] == "[":
        return (is_vertically_moveable(grid, next, direction) and
        is_vertically_moveable(grid, (next[0], next[1] + 1), direction))
    else:
        return is_vertically_moveable(grid, next, direction)
    

def move_vertically(grid, pos, direction):
    next = Grids.get_adjacent_points(pos)[direction]

    if grid[next] == ".":
        grid[next] = grid[pos]
    elif grid[pos] == "@" and grid[next] == "]":
        move_vertically(grid, next, direction)
        move_vertically(grid, (next[0], next[1] - 1), direction)

        grid[next] = "@"
        grid[pos] = "."
        grid[(next[0], next[1] - 1)] = "."
    elif grid[pos] == "@" and grid[next] == "[":
        move_vertically(grid, next, direction)
        move_vertically(grid, (next[0], next[1] + 1), direction)

        grid[next] = "@"
        grid[pos] = "."
        grid[(next[0], next[1] + 1)] = "."
    elif grid[pos] == "[" and grid[next] == "]":
        move_vertically(grid, next, direction)
        move_vertically(grid, (next[0], next[1] - 1), direction)
        
        grid[next] = grid[pos]
        grid[(next[0], next[1] - 1)] = "."
    elif grid[pos] == "]" and grid[next] == "[":
        move_vertically(grid, next, direction)
        move_vertically(grid, (next[0], next[1] + 1), direction)

        grid[next] = grid[pos]
        grid[(next[0], next[1] + 1)] = "."
    else:
        move_vertically(grid, next, direction)
        grid[next] = grid[pos]


def star_two(filepath):
    grid, moves, robot_pos = gen_grid(filepath)
    grid, robot_pos = make_wide_grid(grid, robot_pos)

    for move in moves:
        if move == "v" or move == "^":
            if not is_vertically_moveable(grid, robot_pos, moves_map[move]):
                continue
            move_vertically(grid, robot_pos, moves_map[move])
            grid[robot_pos] = "."
            robot_pos = Grids.get_adjacent_points(robot_pos)[moves_map[move]]
        else:
            path = []
            pos_to_check = robot_pos
            while True:
                path.append(pos_to_check)
                pos_to_check = Grids.get_adjacent_points(pos_to_check)[moves_map[move]]
                
                if grid[pos_to_check] == ".":
                    path.append(pos_to_check)
                    robot_pos = path[1]
                    for i in range(len(path) - 1, 1, -1):
                        grid[path[i]] = grid[path[i - 1]]
                    grid[path[0]] = '.'
                    grid[path[1]] = '@'
                    break
                if grid[pos_to_check] == "#":
                    break

    return cal_gps_sum(grid)


if __name__ == "__main__":
    print(star_one("inputs/Day15.txt"))
    print(star_two("inputs/Day15.txt"))
