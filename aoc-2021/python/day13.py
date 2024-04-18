import numpy as np

dots, instructions = open('./input/day13.txt').read().split('\n\n')
dots = {(int(x.split(',')[0]), int(x.split(',')[1])) for x in dots.split('\n')}
instructions = [line.split()[2] for line in instructions.split('\n')]

def part_one():
    axis, indx = instructions[0].split('=')
    indx = int(indx)
    folded = set()
    for x, y in dots:
        if axis == 'x' and x > indx:
            x = 2*indx - x
        elif axis == 'y' and y > indx:
            y = 2*indx - y
        folded.add((x, y))
    print(len(folded))
    
part_one()

def part_two():
    global dots
    for instruction in instructions:
        axis, indx = instruction.split('=')
        indx = int(indx)
        folded = set()
        for x, y in dots:
            if axis == 'x' and x > indx:
                x = 2*indx - x
            elif axis == 'y' and y > indx:
                y = 2*indx - y
            folded.add((x, y))
        dots = folded
    h, w = 0, 0
    for x, y in dots:
        h = max(x, h)
        w = max(y, w)
    h, w = h+1, w+1
    grid = [['.']*w for _ in range(h)]
    for x, y in dots:
        grid[x][y] = '#'
    res = ''
    for j in range(w):
        for i in range(h):
            res += grid[i][j]
        res += '\n'
    print(res)
    
part_two()

