import re


registers = {
    "A": None,
    "B": None,
    "C": None,
}
numbers_to_registers = ["A", "B", "C"]
instruction_ptr = 0


def read_system_details(filepath):
    with open(filepath) as file:
        contents = file.read()
        
        regs = re.findall("Register ([A-C]): ([0-9]+)", contents)
        for reg in regs:
            registers[reg[0]] = int(reg[1])

        program = re.findall("Program: (.*)", contents)
        program = re.findall("([0-9]+),?", program[0])
        program = [int(op) for op in program]
    
    return program


def get_combo_op(x):
    if x <= 3:
        return x
    if x == 7:
        return -100
    return registers[numbers_to_registers[x - 4]]


def division(reg, x):
    registers[reg] = int(registers["A"] / (2 ** get_combo_op(x)))


def adv(x):
    division("A", x)


def bdv(x):
    division("B", x)


def cdv(x):
    division("C", x)


def bxl(x):
    registers["B"] = registers["B"] ^ x


def bst(x):
    registers["B"] = get_combo_op(x) % 8


def jnz(x):
    if registers["A"] == 0:
        return
    global instruction_ptr
    instruction_ptr = x - 2


def bxc(_):
    registers["B"] = registers["B"] ^ registers["C"]


def out(x):
    return get_combo_op(x) % 8


opcode_to_func = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}


def run_program(program, break_if_pal = False):
    result = []
    global instruction_ptr
    instruction_ptr = 0
    while instruction_ptr < len(program):
        output = opcode_to_func[program[instruction_ptr]](program[instruction_ptr + 1])
        if output != None:
            if break_if_pal and output != program[len(result)]:
                return None
            result.append(output)
        instruction_ptr += 2

    return result


def star_one(filepath):
    program = read_system_details(filepath)
    return ",".join([str(i) for i in run_program(program)])


def star_two(_):
    values = [2,4,1,2,7,5,0,3,4,7,1,7,5,5,3,0]

    a_init = 0
    while True:
        a = a_init
        b = 0
        c = 0
        for i in range(17):
            if i == 16:
                return a_init
            b = (a % 8) ^ 2
            c = int(a / (2 ** b))
            a = int(a / 8)
            b = b ^ c
            b = b ^ 7
            if (b % 8) != values[i]:
                break
        a_init += 1

def fuck_this_shit():
    values = [2,4,1,2,7,5,0,3,4,7,1,7,5,5,3,0]

    a_init = 0
    diffs = [1]
    d = 0
    best_i = 0
    last = 0
    while True:
        a = a_init
        b = 0
        c = 0
        for i in range(len(values) + 1):
            if i == 1:
                diff = a_init - last
                print(diff)
                last = a_init
            # if i == best_i + 1:
            #     diff = a_init - last
            #     last = a_init
            #     if diffs[i][0] == diff:
            #         best
            # if i == len(values):
            #     return a_init
            # if i == a_last_best_value[1] and i < 2:
            #     if a_last_best_value[0] == None:
            #         a_last_best_value = (a_init, i)
            #     else:
            #         diff = a_init - a_last_best_value[0]
            #         a_last_best_value = (None, i + 1)                  
            b = (a % 8) ^ 2
            c = int(a / (2 ** b))
            a = int(a / 8)
            b = b ^ c
            b = b ^ 7
            if (b % 8) != values[i]:
                break
        a_init += diffs[d % len(diffs)]
        d += 1


if __name__ == "__main__":
    print(star_one("inputs/Day17.txt"))
    fuck_this_shit()
    print(star_two("inputs/Day17.txt"))
