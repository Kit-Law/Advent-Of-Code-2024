
def gen_grid(filepath):
    grid = []
    pos = [0, 0]

    with open(filepath) as file:
        for y, line in enumerate(file):
            try:
                starting_pos = line.index("^")
                pos = [y, starting_pos]
            except:
                pass
            grid.append(list(line.rstrip()))
    
    return (grid, pos)


def star_one(filepath):
    grid, pos = gen_grid(filepath)
    direction = 'N'
    steps = set()
    steps.add((pos[0], pos[1]))

    while True:
        if direction == 'N':
            if pos[0] - 1 < 0:
                break
            if grid[pos[0] - 1][pos[1]] == '#':
                direction = 'E'
            else:
                pos[0] -= 1
                steps.add((pos[0], pos[1]))
        elif direction == 'E':
            if pos[1] + 1 >= len(grid[0]):
                break
            if grid[pos[0]][pos[1] + 1] == '#':
                direction = 'S'
            else:
                pos[1] += 1
                steps.add((pos[0], pos[1]))
        elif direction == 'S':
            if pos[0] + 1 >= len(grid):
                break
            if grid[pos[0] + 1][pos[1]] == '#':
                direction = 'W'
            else:
                pos[0] += 1
                steps.add((pos[0], pos[1]))
        else:
            if pos[1] - 1 < 0:
                break
            if grid[pos[0]][pos[1] - 1] == '#':
                direction = 'N'
            else:
                pos[1] -= 1
                steps.add((pos[0], pos[1]))

    return len(steps)


def is_moving_into_loop(steps, pos, direction):
    buff = (pos[0], pos[1], direction)
    if buff in steps:
        return True
    steps.add(buff)
    return False


def is_infinite_loop(grid, pos):
    direction = 'N'
    steps = set()
    steps.add((pos[0], pos[1], direction))

    while True:
        if direction == 'N':
            if pos[0] - 1 < 0:
                return False
            if grid[pos[0] - 1][pos[1]] == '#':
                direction = 'E'
            else:
                pos[0] -= 1
                if is_moving_into_loop(steps, pos, direction):
                    return True
        elif direction == 'E':
            if pos[1] + 1 >= len(grid[0]):
                return False
            if grid[pos[0]][pos[1] + 1] == '#':
                direction = 'S'
            else:
                pos[1] += 1
                if is_moving_into_loop(steps, pos, direction):
                    return True
        elif direction == 'S':
            if pos[0] + 1 >= len(grid):
                return False
            if grid[pos[0] + 1][pos[1]] == '#':
                direction = 'W'
            else:
                pos[0] += 1
                if is_moving_into_loop(steps, pos, direction):
                    return True
        else:
            if pos[1] - 1 < 0:
                return False
            if grid[pos[0]][pos[1] - 1] == '#':
                direction = 'N'
            else:
                pos[1] -= 1
                if is_moving_into_loop(steps, pos, direction):
                    return True


def star_two(filepath):
    grid, pos = gen_grid(filepath)

    number_of_loops = 0

    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == '#' or grid[j][i] == '^':
                continue
            grid[j][i] = '#'
            if is_infinite_loop(grid, [pos[0], pos[1]]):
                number_of_loops += 1
            grid[j][i] = '.'

    return number_of_loops


if __name__=="__main__":
    print(star_one("inputs/Day6.txt"))
    print(star_two("inputs/Day6.txt"))
