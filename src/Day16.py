import Helpers.Grids as Grids


def gen_maze(filepath):
    grid = Grids.Grid()
    start = (0, 0)
    end = (0, 0)

    with open(filepath) as file:
        for y, line in enumerate(file):
            try:
                starting_pos = line.index("S")
                start = (y, starting_pos)
            except:
                pass
            try:
                ending_pos = line.index("E")
                end = (y, ending_pos)
            except:
                pass

            grid.append(list(line.rstrip()))

    return (grid, start, end)


def calculate_cost(previous_pos, pos, heuristic_cost, move):
    is_straight_line = (previous_pos[0] == pos[0] and pos[0] == move[0]) or (previous_pos[1] == pos[1] and pos[1] == move[1])
    turn_cost = 0 if is_straight_line else 1000
    return turn_cost + 1 + heuristic_cost


# For some reason this is wrong by 4 sometimes?
def traverse_maze(maze, pos, previous_pos, end):
    edges = [(previous_pos, pos, 0)]
    while len(edges) > 0:
        edges.sort(key=lambda x: x[2])
        edge = edges[0]
        while True:
            if pos == end:
                break

            possible_moves = [point for point in Grids.get_adjacent_points(edge[1]) if maze[point] != "#" and point != edge[0]]
            is_fully_explored = True
            
            for move in possible_moves:
                cost = calculate_cost(edge[0], edge[1], edge[2], move)
                if type(maze[move]) == int and cost >= maze[move]:
                    continue
                maze[move] = cost
                edges.append((edge[1], move, cost))
                is_fully_explored = False

            if is_fully_explored:
                break

            edge = edges[-1]
            edges = edges[:-1]
        edges = edges[1:]


def star_one(filepath):
    maze, start, end = gen_maze(filepath)

    maze[start] = 0
    maze[end] = "."
    print(end)
    traverse_maze(maze, start, (start[0], start[1] - 1), end)

    return maze[end]


def traverse_shortest_path(maze, previous_pos, pos, end, best_seats):
    if pos == end:
        return
    
    possible_moves = [point for point in Grids.get_adjacent_points(pos) if type(maze[point]) == int]
    for move in possible_moves:
        #if move[0] == 
        if (maze[pos] - 1 == maze[move]) or (maze[pos] - 1001 == maze[move]):
            best_seats.add(move)
            traverse_shortest_path(maze, pos, move, end, best_seats)


def star_two(filepath):
    maze, start, end = gen_maze(filepath)

    maze[start] = 0
    maze[end] = "."
    traverse_maze(maze, start, (start[0], start[1] - 1))

    best_seats = set()
    traverse_shortest_path(maze, end, end, start, best_seats)

    for j, line in enumerate(maze):
        for i, c in enumerate(line):
            if (j, i) in best_seats:
                print("O", end = '')
            elif type(c) == int:
                print(".", end = '')
            else:
                print(c, end='')
        print("")

    return len(best_seats)





import heapq


def parse(lines):
    grid = []
    line = 0
    for line in range(len(lines)):
        grid.append(list(lines[line].strip()))

    s = None
    e = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                s = (r, c)
            elif ch == "E":
                e = (r, c)
    return grid, s, e


def dijkstra(grid, starts):
    delta = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}

    dist = {}
    pq = []
    for sr, sc, dir in starts:
        dist[(sr, sc, dir)] = 0
        heapq.heappush(pq, (0, sr, sc, dir))

    while pq:
        (d, row, col, direction) = heapq.heappop(pq)
        if dist[(row, col, direction)] < d:
            continue
        for next_dir in "EWNS".replace(direction, ""):
            if (row, col, next_dir) not in dist or dist[
                (row, col, next_dir)
            ] > d + 1000:
                dist[(row, col, next_dir)] = d + 1000
                heapq.heappush(pq, (d + 1000, row, col, next_dir))
        dr, dc = delta[direction]
        next_row, next_col = row + dr, col + dc
        if (
            0 <= next_row < len(grid)
            and 0 <= next_col < len(grid[0])
            and grid[next_row][next_col] != "#"
            and (
                (next_row, next_col, direction) not in dist
                or dist[(next_row, next_col, direction)] > d + 1
            )
        ):
            dist[(next_row, next_col, direction)] = d + 1
            heapq.heappush(pq, (d + 1, next_row, next_col, direction))

    return dist


def part1(input):
    grid, (sr, sc), (er, ec) = input
    dist = dijkstra(grid, [(sr, sc, "E")])
    best = 1000000000
    for dir in "EWNS":
        if (er, ec, dir) in dist:
            best = min(best, dist[(er, ec, dir)])
    return best

real = parse(open("inputs/Day16.txt").readlines())
input = real


if __name__ == "__main__":
    what = star_one("inputs/Day16.txt")
    print(what)
    tf = part1(input)
    print(tf)
    print(what == tf)
    print(70281)