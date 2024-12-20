import re


def read_claw_machines(filepath):
    with open(filepath) as file:
        contents = file.read()
        instances = re.findall(
            "Button A: X\+([0-9]*), Y\+([0-9]*)\nButton B: X\+([0-9]*), Y\+([0-9]*)\nPrize: X=([0-9]*), Y=([0-9]*)",
            contents,
        )
        instances = [
            (get_moves(instance), [int(instance[4]), int(instance[5])])
            for instance in instances
        ]
    return instances


def get_moves(regex_capture):
    return (
        (int(regex_capture[0]), int(regex_capture[1]), 3),
        (int(regex_capture[2]), int(regex_capture[3]), 1),
    )


def liner_alg_solve_machine(a, b, x, y):
    num_a_presses = round(((b[1] * x / b[0]) - y) / ((b[1] * a[0]) / b[0] - a[1]))
    num_b_presses = round((x - a[0] * num_a_presses) / b[0])

    if x != num_a_presses * a[0] + num_b_presses * b[0]:
        return None
    if y != num_a_presses * a[1] + num_b_presses * b[1]:
        return None

    return num_a_presses * 3 + num_b_presses


def star_one(filepath):
    tokens = 0
    instances = read_claw_machines(filepath)

    for (a, b), target in instances:
        tokens_needed = liner_alg_solve_machine(a, b, target[0], target[1])

        if tokens_needed:
            tokens += tokens_needed

    return int(tokens)


def star_two(filepath):
    tokens = 0
    instances = read_claw_machines(filepath)

    for (a, b), target in instances:
        tokens_needed = liner_alg_solve_machine(
            a, b, target[0] + 10000000000000, target[1] + 10000000000000
        )

        if tokens_needed:
            tokens += tokens_needed

    return int(tokens)


if __name__ == "__main__":
    print(star_one("inputs/Day13.txt"))
    print(star_two("inputs/Day13.txt"))
