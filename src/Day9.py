def sum_over_range(a, b, v=1):
    sum = 0
    for i in range(a, b):
        sum += i * v
    return sum


def star_one(filepath):
    final_sum = 0

    files = []
    emptys = []

    with open(filepath) as file:
        line = file.read()
        for i in range(0, len(line), 2):
            files.append(int(line[i]))
            if i + 1 < len(line):
                emptys.append(int(line[i + 1]))

    index = 0
    id = 0
    while True:
        file = files[id]
        empty = emptys[id]

        final_sum += sum_over_range(index, index + file, id)
        index += file
        id += 1

        if id >= len(files):
            break

        while files[-1] <= empty:
            final_sum += sum_over_range(index, index + files[-1], len(files) - 1)
            index += files[-1]
            empty -= files[-1]
            del files[-1]

        final_sum += sum_over_range(index, index + empty, len(files) - 1)
        index += empty
        files[-1] -= empty

    return final_sum


def star_two(filepath):
    files = []

    with open(filepath) as file:
        line = file.read()
        for i in range(0, len(line), 2):
            files.append([i / 2, int(line[i])])
            if i + 1 < len(line):
                files.append([None, int(line[i + 1])])

    j = len(files) - 1
    while j > 0:
        if files[j][0] == None:
            j -= 1
            continue
        for i in range(j):
            if files[i][0] != None:
                continue
            if files[j][1] > files[i][1]:
                continue
            new_empty = [None, files[i][1] - files[j][1]]
            files[i][0] = files[j][0]
            files[i][1] = files[j][1]
            files[j][0] = None
            if new_empty[1] > 0:
                files.insert(i + 1, new_empty)
            break
        j -= 1

    final_sum = 0
    index = 0
    for file in files:
        if file[0]:
            final_sum += sum_over_range(index, index + file[1], file[0])
        index += file[1]

    return int(final_sum)


if __name__ == "__main__":
    print(star_one("inputs/Day9.txt"))
    print(star_two("inputs/Day9.txt"))
