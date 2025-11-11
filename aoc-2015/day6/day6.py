import numpy as np
from time import time

n = 1000
lines = [x.split(' ') for x in open('aoc-2015/input/day6.txt')]

def solve(g):
    t = time()
    for line in lines:
        mode = line[1]
        f = g(mode)
        x1, y1 = [int(x) for x in line[-3].split(',')]
        x2, y2 = [int(x) for x in line[-1].split(',')]
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                grid[i][j] = f(grid[i][j])
    print(np.sum(grid), time() - t)

fs = [
    lambda mode: (lambda _: 1) if mode == 'on' else ((lambda _: 0) if mode == 'off' else (lambda x: (x + 1) % 2)),
    lambda mode: (lambda x: x+1) if mode == 'on' else ((lambda x: max(0, x-1)) if mode == 'off' else (lambda x: x+2))
]

for f in fs:
    grid = [[0 for _ in range(n)] for _ in range(n)]
    solve(f)