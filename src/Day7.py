

def is_number_correct(goal, current, numbers):
    if not numbers:
        return goal == current
    
    if is_number_correct(goal, current + numbers[0], numbers[1:]):
        return True
    return is_number_correct(goal, current * numbers[0], numbers[1:])


def is_number_correct_concat(goal, current, numbers):
    if not numbers:
        return goal == current
    
    if is_number_correct_concat(goal, current + numbers[0], numbers[1:]):
        return True
    if is_number_correct_concat(goal, current * numbers[0], numbers[1:]):
        return True
    return is_number_correct_concat(goal, int(str(current) + str(numbers[0])), numbers[1:])


def star_one(filepath):
    result = 0

    with open(filepath) as file:
        for line in file:
            (goal, numbers) = line.rstrip().split(":")
            numbers = [int(number) for number in numbers[1:].split(" ")]

            if is_number_correct(int(goal), int(numbers[0]), numbers[1:]):
                result += int(goal)

    return result


def star_two(filepath):
    result = 0

    with open(filepath) as file:
        for line in file:
            (goal, numbers) = line.rstrip().split(":")
            numbers = [int(number) for number in numbers[1:].split(" ")]
            
            if is_number_correct_concat(int(goal), int(numbers[0]), numbers[1:]):
                result += int(goal)

    return result


if __name__=="__main__":
    print(star_one("inputs/Day7.txt"))
    print(star_two("inputs/Day7.txt"))
