from collections import defaultdict


def get_antenna(filepath):
    antennas = defaultdict(list)

    length = 0
    height = 0

    with open(filepath) as file:
        for y, line in enumerate(file):
            height += 1
            for x, c in enumerate(list(line.rstrip())):
                if c == '.' or c == '#':
                    continue
                antennas[c].append((x, y))
                length = len(line)

        return (antennas, (length, height))


def is_in_bounds(p, bounds):
    return (p[0] >= 0 and p[0] < bounds[0] and
        p[1] >= 0 and p[1] < bounds[1])


def cal_next_point(p1, p2):
    return tuple(p1_i - p2_i + p1_i for p1_i, p2_i in zip(p1, p2))


def star_one(filepath):
    antennas, bounds = get_antenna(filepath)
    points = set()
    
    for antenna in antennas.values():
        for p1 in antenna:
            for p2 in antenna:
                if p1 == p2:
                    continue
                p12 = cal_next_point(p1, p2)
                if is_in_bounds(p12, bounds):
                    points.add(p12)

    return len(points)


def star_two(filepath):
    antennas, bounds = get_antenna(filepath)
    points = set()
    
    for antenna in antennas.values():
        for p1 in antenna:
            for p2 in antenna:
                if p1 == p2:
                    continue
                pa = p1
                pb = p2
                while is_in_bounds(pa, bounds):
                    points.add(pa)
                    pbuffer = pa
                    pa = cal_next_point(pbuffer,  pb)
                    pb = pbuffer

    return len(points)


if __name__=="__main__":
    print(star_one("inputs/Day8.txt"))
    print(star_two("inputs/Day8.txt"))
