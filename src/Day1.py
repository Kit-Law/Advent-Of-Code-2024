def star_one(filepath):
    ls = []
    rs = []

    with open(filepath) as file:
        for line in file:
            lhs, rhs = line.rstrip().split("   ")
            ls.append(int(lhs))
            rs.append(int(rhs))

    ls.sort()
    rs.sort()

    result = 0

    for i in range(len(ls)):
        result += abs(ls[i] - rs[i])

    return result


def star_two(filepath):
    keys = {}
    values = []

    with open(filepath) as file:
        for line in file:
            lhs, rhs = line.rstrip().split("   ")
            keys[lhs] = 0
            values.append(rhs)

    for value in values:
        if value not in keys:
            continue

        keys[value] = keys[value] + 1

    result = 0

    for key, value in keys.items():
        result += int(key) * value

    return result


if __name__ == "__main__":
    print(star_one("inputs/Day1.txt"))
    print(star_two("inputs/Day1.txt"))
