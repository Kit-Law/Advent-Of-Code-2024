import re


def read_guard_poses(filepath):
    with open(filepath) as file:
        contents = file.read()
        guard_info = re.findall(
            "p=([0-9]+),([0-9]+) v=([0-9\-]+),([0-9\-]+)",
            contents,
        )
        guards = [
            (int(px), int(py), int(vx), int(vy))
            for px, py, vx, vy in guard_info
        ]
    return guards


def get_guard_positions_at(guards, seconds, grid_size_x, grid_size_y):
    positions = []
    for px, py, vx, vy in guards:
        x = (px + (vx * seconds)) % grid_size_x
        y = (py + (vy * seconds)) % grid_size_y
        positions.append((x, y))
    return positions


def cal_guards_per_quadrants(positions, grid_size_x, grid_size_y):
    grid_size_x = int(grid_size_x / 2)
    grid_size_y = int(grid_size_y / 2)

    guards_per_quadrants = [0, 0, 0, 0]

    for x, y in positions:
        if x < grid_size_x and y < grid_size_y:
            guards_per_quadrants[0] += 1
        elif x < grid_size_x and y > grid_size_y:
            guards_per_quadrants[1] += 1
        elif x > grid_size_x and y < grid_size_y:
            guards_per_quadrants[2] += 1
        elif x > grid_size_x and y > grid_size_y:
            guards_per_quadrants[3] += 1

    return guards_per_quadrants


def print_guards(positions, grid_size_x, grid_size_y):
    for j in range(grid_size_y):
        for i in range(grid_size_x):
            if (i, j) in positions:
                print("#", end='')
            else:
                print(".", end='')
        print("")


def star_one(filepath):
    guards = read_guard_poses(filepath)
    positions = get_guard_positions_at(guards, 100, 101, 103)

    guards_per_quadrants = cal_guards_per_quadrants(positions, 101, 103)

    total = 1
    for guards_per_quadrant in guards_per_quadrants:
        total *= guards_per_quadrant

    return int(total)


def star_two(filepath):
    guards = read_guard_poses(filepath)
    lowest_entropy = (None, None)

    for seconds in range(10000):
        positions = get_guard_positions_at(guards, seconds, 101, 103)
        qs = cal_guards_per_quadrants(positions, 101, 103)
        # hardcoding for performance
        total = qs[0] * qs[1] * qs[2] * qs[3]
        
        if not lowest_entropy[0] or total < lowest_entropy[0]:
            lowest_entropy = (total, seconds)

    return lowest_entropy[1]

if __name__ == "__main__":
    print(star_one("inputs/Day14.txt"))
    print(star_two("inputs/Day14.txt"))
