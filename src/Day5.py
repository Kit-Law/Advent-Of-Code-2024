import math
from collections import defaultdict


def parse_input_file(filepath):
    ordering_rules = defaultdict(list)
    lines = []
    is_ordering_rule = True

    with open(filepath) as file:
        for line in file:
            if is_ordering_rule:
                values = line.rstrip().split("|")
                if values == [""]:
                    is_ordering_rule = False
                    continue
                ordering_rules[values[0]].append(values[1])
            else:
                lines.append(line.rstrip().split(","))

    return (ordering_rules, lines)


def check_correct_order(line, ordering_rules):
    wrong_orders = []
    seen = set()

    for num in line:
        if num in ordering_rules:
            for rule in ordering_rules[num]:
                if rule in seen:
                    wrong_orders.append((num, rule))
                    break
        seen.add(num)

    return wrong_orders


def swap_elements(ls, lhs, rhs):
    lhs_index, rhs_index = ls.index(lhs), ls.index(rhs)
    ls[rhs_index], ls[lhs_index] = ls[lhs_index], ls[rhs_index]


def star_one(filepath):
    total = 0

    (ordering_rules, lines) = parse_input_file(filepath)

    for line in lines:
        wrong_orderings = check_correct_order(line, ordering_rules)
        if not wrong_orderings:
            total += int(line[math.floor(len(line) / 2)])

    return total


def star_two(filepath):
    total = 0

    (ordering_rules, lines) = parse_input_file(filepath)

    for line in lines:
        wrong_orderings = check_correct_order(line, ordering_rules)
        if wrong_orderings:
            while wrong_orderings:
                for order in wrong_orderings:
                    swap_elements(line, order[0], order[1])
                wrong_orderings = check_correct_order(line, ordering_rules)

            total += int(line[math.floor(len(line) / 2)])

    return total


if __name__ == "__main__":
    print(star_one("inputs/Day5.txt"))
    print(star_two("inputs/Day5.txt"))
