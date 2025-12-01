grid = [[int(y) for y in list(x.rstrip())] for x in open(path + '/day11.txt')]
n, m = len(grid), len(grid[0])

def part_one():
    count = 0
    for _ in range(100):
        flashing, flashed = set(), set()
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                grid[i][j] += 1
                if grid[i][j] > 9:
                    flashing.add((i, j))
        while flashing:
            i, j = flashing.pop()
            if (i, j) in flashed:
                continue
            flashed.add((i, j))
            neighbors = [
                (i+1, j), (i-1, j), (i, j-1), (i, j+1),
                (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)
            ]
            for x, y in neighbors:
                if 0 <= x < n and 0 <= y < m:
                    grid[x][y] += 1
                    if grid[x][y] > 9 and (x, y) not in flashed:
                        flashing.add((x, y))
        for i, j in flashed:
            grid[i][j] = 0
        count += len(flashed)
    print(count)
    
def part_two():
    count = 0
    while(True):
        count += 1
        flashing, flashed = set(), set()
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                grid[i][j] += 1
                if grid[i][j] > 9:
                    flashing.add((i, j))
        while flashing:
            i, j = flashing.pop()
            if (i, j) in flashed:
                continue
            flashed.add((i, j))
            neighbors = [
                (i+1, j), (i-1, j), (i, j-1), (i, j+1),
                (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)
            ]
            for x, y in neighbors:
                if 0 <= x < n and 0 <= y < m:
                    grid[x][y] += 1
                    if grid[x][y] > 9 and (x, y) not in flashed:
                        flashing.add((x, y))
        for i, j in flashed:
            grid[i][j] = 0
        if len(flashed) == m*n:
            break
    print(count)
    
# part_one()
part_two()