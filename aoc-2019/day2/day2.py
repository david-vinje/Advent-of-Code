import os

path = os.path.dirname(os.path.abspath(__file__))

programs = [
    [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
    [1, 0, 0, 0, 99],
    [2, 3, 0, 3, 99],
    [2, 4, 4, 5, 99, 0],
    [1, 1, 1, 4, 99, 5, 6, 0, 99],
    [int(x) for x in open(path + '/day2.txt').read().split(",")],
]

def part_one(program):
    i = 0
    opcode = program[0]
    while opcode != 99:
        a, b, c = [program[i + x] for x in range(1, 4)]
        if opcode == 1:
            program[c] = program[a] + program[b]
        elif opcode == 2:
            program[c] = program[a] * program[b]
        else:
            raise "Whoops, something went wrong"
        i += 4
        opcode = program[i]
    print(program[0])
    

for program in programs:
    part_one(program)
