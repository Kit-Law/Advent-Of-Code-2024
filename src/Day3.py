import re


def star_one(filepath):
    with open(filepath) as file:
        contents = file.read()
        values = re.findall("mul\(([0-9]+),([0-9]+)\)", contents)
    
    return sum(map(lambda v: int(v[0]) * int(v[1]), values))


def star_two(filepath):
    with open(filepath) as file:
        contents = file.read()
        values = re.findall("(mul\(([0-9]+),([0-9]+)\))|(do\(\))|(don't\(\))", contents)
    
    is_do = True
    result = 0
    for value in values:
        if value[0] and is_do:
            result += int(value[1]) * int(value[2])
        elif value[3]:
            is_do = True
        elif value[4]:
            is_do = False

    return result


if __name__=="__main__":
    print(star_one("inputs/Day3.txt"))
    print(star_two("inputs/Day3.txt"))
