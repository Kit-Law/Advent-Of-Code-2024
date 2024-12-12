

dp_stones = {}


class Stone:
    def __init__(this, value, remaining_turns):
        this.value = value
        this.remaining_turns = remaining_turns


def init_stones(filepath, n):
    with open(filepath) as file:
        stones = [Stone(stone, n) for stone in file.read().rstrip().split(" ")]
    
    return stones


def blink_n_times(filepath, n):
    number_of_stones = 0
    for stone in init_stones(filepath, n):
        number_of_stones += traverse_path(stone)

    return number_of_stones


def perform_zero_rule(stone):
    if stone.value == "0":
        stone.value = "1"
        return True
    return False


def perform_splitting_rule(stone):
    if len(stone.value) % 2 != 0:
        return 0
    
    lhs = stone.value[:int(len(stone.value) / 2)]
    rhs = str(int(stone.value[int(len(stone.value) / 2):]))

    stone.value = lhs
    number_of_stones = traverse_path(Stone(rhs, stone.remaining_turns - 1))

    return number_of_stones


def perform_basic_turn(stone):
    if perform_zero_rule(stone):
        return 0
    
    number_of_stones = perform_splitting_rule(stone)
    if number_of_stones > 0:
        return number_of_stones
    
    stone.value = str(int(stone.value) * 2024)
    return 0


def traverse_path(stone):
    if (stone.value, stone.remaining_turns) in dp_stones:
        return dp_stones[(stone.value, stone.remaining_turns)]

    origin = (stone.value, stone.remaining_turns)
    number_of_stones = 1

    while stone.remaining_turns > 0:
        number_of_stones += perform_basic_turn(stone)
        stone.remaining_turns -= 1

    dp_stones[origin] = number_of_stones

    return number_of_stones


def star_one(filepath):
    return blink_n_times(filepath, 25)


def star_two(filepath):
    return blink_n_times(filepath, 75)


if __name__=="__main__":
    print(star_one("inputs/Day11.txt"))
    print(star_two("inputs/Day11.txt")) 
