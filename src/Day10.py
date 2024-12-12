import Helpers.Grids as Grids


grid = Grids.Grid()
seen = set()


def gen_grid(filepath):
    zeros = []
    grid.clear()

    with open(filepath) as file:
        for y, line in enumerate(file):
            zeros += [(y, x) for x, l in enumerate(line) if l == "0"]
            grid.append([int(l) for l in line.rstrip()])
    
    return zeros


def traverse_steps(pos, current_level, all_paths = False):
    if current_level == 9:
        if not all_paths and pos in seen:
            return 0
        seen.add(pos)
        return 1
    
    number_of_paths = 0

    for neighbor in Grids.get_cardinal_neighbors(pos, grid):
        if grid[neighbor] == current_level + 1:
            number_of_paths += traverse_steps(neighbor, current_level + 1, all_paths)

    return number_of_paths


def star_one(filepath):
    zeros = gen_grid(filepath)
    headtails = 0

    for zero in zeros:
        headtails += traverse_steps(zero, 0)
        seen.clear()

    return headtails


def star_two(filepath):
    zeros = gen_grid(filepath)
    headtails = 0

    for zero in zeros:
        headtails += traverse_steps(zero, 0, True)

    return headtails


if __name__=="__main__":
    print(star_one("inputs/Day10.txt"))
    print(star_two("inputs/Day10.txt")) 
