import Helpers.Grids as Grids


def gen_grid(filepath):
    grid = Grids.Grid()
    pos = (0, 0)

    with open(filepath) as file:
        for y, line in enumerate(file):
            try:
                starting_pos = line.index("^")
                pos = (y, starting_pos)
            except:
                pass
            grid.append(list(line.rstrip()))

    return (grid, pos)


def turn_nighty_degrees(direction):
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    else:
        return "N"


def star_one(filepath):
    grid, pos = gen_grid(filepath)
    direction = "N"
    steps = set()
    steps.add(pos)

    while True:
        surroundings = Grids.get_adjacent_points(pos)
        if not surroundings.is_in_range(direction, grid):
            break

        if grid[surroundings[direction]] == "#":
            direction = turn_nighty_degrees(direction)
        else:
            pos = surroundings[direction]
            steps.add(pos)

    return len(steps)


def is_moving_into_loop(steps, pos, direction):
    buff = (pos[0], pos[1], direction)
    if buff in steps:
        return True
    steps.add(buff)
    return False


def is_infinite_loop(grid, pos):
    direction = "N"
    steps = set()
    steps.add((pos[0], pos[1], direction))

    while True:
        surroundings = Grids.get_adjacent_points(pos)
        if not surroundings.is_in_range(direction, grid):
            return False

        if grid[surroundings[direction]] == "#":
            direction = turn_nighty_degrees(direction)
        else:
            pos = surroundings[direction]
            if is_moving_into_loop(steps, pos, direction):
                return True


def star_two(filepath):
    grid, pos = gen_grid(filepath)

    number_of_loops = 0

    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == "#" or grid[j][i] == "^":
                continue
            grid[j][i] = "#"
            if is_infinite_loop(grid, [pos[0], pos[1]]):
                number_of_loops += 1
            grid[j][i] = "."

    return number_of_loops


if __name__ == "__main__":
    print(star_one("inputs/Day6.txt"))
    print(star_two("inputs/Day6.txt"))
