import dataclasses
import re

InputData = tuple[tuple[int, int, int], list[int]]

def read_input() -> str:
    with open("inputs/Day17.txt", encoding="utf-8") as f:
        return f.read()



def get_parsed_input() -> InputData:
    input_raw = read_input()
    registers_str, program_str = input_raw.strip().split("\n\n")
    a, b, c = map(int, re.findall(r"Register [ABC]: (\d+)", registers_str))
    program = list(map(int, program_str.removeprefix("Program: ").split(",")))
    return (a, b, c), program


@dataclasses.dataclass
class Registers:
    a: int
    b: int
    c: int

    @classmethod
    def from_tuple(cls, tup: tuple[int, int, int]):
        a, b, c = tup
        return cls(a=a, b=b, c=c)

    def get_combo_operand(self, operand: int) -> int:
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        else:
            raise ValueError(f"invalid operand: {operand}")


# part 1


def run(registers_tup: tuple[int, int, int], program: list[int]) -> list[int]:
    registers = Registers.from_tuple(registers_tup)
    ptr = 0
    output = []
    while True:
        # check halting status / get next input
        try:
            opcode = program[ptr]
            operand = program[ptr + 1]
        except IndexError:
            break
        # do the thing
        ptr_next = ptr + 2
        if opcode == 0:  # adv
            registers.a = int(registers.a / (2 ** registers.get_combo_operand(operand)))
        elif opcode == 1:  # bxl
            registers.b = registers.b ^ operand
        elif opcode == 2:  # bst
            registers.b = registers.get_combo_operand(operand) % 8
        elif opcode == 3:  # jnz
            if registers.a != 0:
                ptr_next = operand
        elif opcode == 4:  # bxc
            registers.b = registers.b ^ registers.c
        elif opcode == 5:  # out
            output.append(registers.get_combo_operand(operand) % 8)
        elif opcode == 6:  # bdv
            registers.b = int(registers.a / (2 ** registers.get_combo_operand(operand)))
        elif opcode == 7:  # cdv
            registers.c = int(registers.a / (2 ** registers.get_combo_operand(operand)))
        else:
            raise ValueError(f"invalid opcode: {opcode}")
        # advance to next instruction
        ptr = ptr_next
    return output

registers_tup, program = get_parsed_input()
# part 1
output = run(registers_tup, program)
print("output:", ",".join(str(o) for o in output))