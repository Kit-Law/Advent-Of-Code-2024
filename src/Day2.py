def star_one(filepath):
    num_of_safe = 0

    with open(filepath) as file:
        for line in file:
            numbers = line.rstrip().split(" ")

            is_ascending = int(numbers[0]) < int(numbers[1])
            is_safe = True

            for i in range(len(numbers) - 1):
                diff = abs(int(numbers[i]) - int(numbers[i + 1]))
                is_currently_ascending = int(numbers[i]) < int(numbers[i + 1])
                if (is_ascending != is_currently_ascending) or diff <= 0 or diff > 3:
                    is_safe = False
                    break

            if is_safe:
                num_of_safe += 1

    return num_of_safe


def star_two(filepath):
    num_of_safe = 0

    with open(filepath) as file:
        for line in file:
            numbers = line.rstrip().split(" ")

            is_ascending = int(numbers[0]) < int(numbers[1])
            is_safe = True
            is_dampener_available = True

            for i in range(len(numbers) - 1):
                diff = abs(int(numbers[i]) - int(numbers[i + 1]))
                is_currently_ascending = int(numbers[i]) < int(numbers[i + 1])
                if (is_ascending != is_currently_ascending) or diff <= 0 or diff > 3:
                    if is_dampener_available:
                        is_dampener_available = False
                        continue
                    is_safe = False
                    break

            if is_safe:
                num_of_safe += 1

    return num_of_safe


if __name__ == "__main__":
    print(star_one("inputs/Day2.txt"))
    print(star_two("inputs/Day2.txt"))
