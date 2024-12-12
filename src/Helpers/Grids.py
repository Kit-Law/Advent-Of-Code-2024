class Grid(list):
    def __getitem__(self, point):
        if type(point) == int:
            return list.__getitem__(self, point)
        return list.__getitem__(self, point[0])[point[1]]


directions = ["N", "E", "S", "W", "NE", "SE", "SW", "NW"]


class AdjacentPoints(list):
    def __getitem__(self, direction):
        if type(direction) == int:
            return list.__getitem__(self, direction)
        return list.__getitem__(self, directions.index(direction))

    def is_in_range(self, direction: str, grid):
        if "N" in direction and self[direction][0] < 0:
            return False

        if "E" in direction and self[direction][1] >= len(grid[0]):
            return False

        if "S" in direction and self[direction][0] >= len(grid):
            return False

        if "W" in direction and self[direction][1] < 0:
            return False

        return True


def read_grid_from_file(filepath):
    grid = Grid()

    with open(filepath) as file:
        for line in file:
            grid.append(list(line.rstrip()))

    return grid


def is_in_range(point, grid, min=0, max=None):
    for component in point:
        if component < min:
            return False

        max = max if max else len(grid)
        if component >= max:
            return False

        try:
            grid = grid[0]
        except:
            return False

    return True


def get_adjacent_points(point, include_diagonals=False):
    points = AdjacentPoints()
    points += [
        (point[0] - 1, point[1]),
        (point[0], point[1] + 1),
        (point[0] + 1, point[1]),
        (point[0], point[1] - 1),
    ]

    if include_diagonals:
        points += [
            (point[0] - 1, point[1] + 1),
            (point[0] + 1, point[1] + 1),
            (point[0] + 1, point[1] - 1),
            (point[0] - 1, point[1] - 1),
        ]

    return points


def get_cardinal_neighbors(point, grid, include_diagonals=False, key=None):
    neighbors = []

    if not key:
        key = lambda y, x, grid: (y, x)

    if point[0] > 0:
        neighbors.append(key(point[0] - 1, point[1], grid))
    if point[0] + 1 < len(grid):
        neighbors.append(key(point[0] + 1, point[1], grid))
    if point[1] > 0:
        neighbors.append(key(point[0], point[1] - 1, grid))
    if point[1] + 1 < len(grid[0]):
        neighbors.append(key(point[0], point[1] + 1, grid))

    if not include_diagonals:
        return neighbors

    if point[0] > 0 and point[1] > 0:
        neighbors.append(key(point[0] - 1, point[1] - 1, grid))
    if point[0] > 0 and point[1] + 1 < len(grid[0]):
        neighbors.append(key(point[0] - 1, point[1] + 1, grid))
    if point[1] > 0 and point[0] + 1 < len(grid):
        neighbors.append(key(point[0] + 1, point[1] - 1, grid))
    if point[0] + 1 < len(grid) and point[1] + 1 < len(grid[0]):
        neighbors.append(key(point[0] + 1, point[1] + 1, grid))

    return neighbors
