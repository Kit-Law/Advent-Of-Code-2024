import re


def rotate(xss):
    result = []

    for y in range(len(xss) - 1, -1, -1):
        rotated_xs = ""
        for x in range(len(xss[0])):
            if x >= len(xss) or y + x >= len(xss[x]):
                break
            rotated_xs += xss[x][y + x]
        result.append(rotated_xs)

    for x in range(len(xss[0]) - 1, 0, -1):
        rotated_xs = ""
        for y in range(len(xss)):
            if y >= len(xss) or y + x >= len(xss[x]):
                break
            rotated_xs += xss[x + y][y]
        result.append(rotated_xs)

    return result


def star_one(filepath):
    occurrences = 0

    with open(filepath) as file:
        lines = [line for line in file.read().splitlines()]

    for line in lines:
        instances = re.findall("XMAS", str(line)) + re.findall("SAMX", str(line))
        occurrences += len(instances)

    transposed_lines = list(map("".join, zip(*reversed(lines))))

    for line in transposed_lines:
        instances = re.findall("XMAS", str(line)) + re.findall("SAMX", str(line))
        occurrences += len(instances)

    lines = rotate(lines)

    for line in lines:
        instances = re.findall("XMAS", str(line)) + re.findall("SAMX", str(line))
        occurrences += len(instances)

    transposed_lines = rotate(transposed_lines)

    for line in transposed_lines:
        instances = re.findall("XMAS", str(line)) + re.findall("SAMX", str(line))
        occurrences += len(instances)

    return occurrences


def star_two(filepath):
    x_mas_count = 0

    with open(filepath) as file:
        lines = [line for line in file.read().splitlines()]

    for j in range(len(lines)):
        for i in range(len(lines[j])):
            if lines[j][i] != "A":
                continue

            if i - 1 < 0 or j - 1 < 0 or i + 1 >= len(lines[j]) or j + 1 >= len(lines):
                continue

            is_downwards = (
                lambda xss, word: xss[j + 1][i + 1] == word[0]
                and xss[j - 1][i - 1] == word[1]
            )
            is_upwards = (
                lambda xss, word: xss[j + 1][i - 1] == word[0]
                and xss[j - 1][i + 1] == word[1]
            )
            is_an_x_max = (is_downwards(lines, "MS") or is_downwards(lines, "SM")) and (
                is_upwards(lines, "MS") or is_upwards(lines, "SM")
            )

            if is_an_x_max:
                x_mas_count += 1

    return x_mas_count


if __name__ == "__main__":
    print(star_one("inputs/Day4.txt"))
    print(star_two("inputs/Day4.txt"))
