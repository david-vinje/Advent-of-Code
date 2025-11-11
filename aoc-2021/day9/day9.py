heightmap = [[int(y) for y in list(x.removesuffix('\n'))] for x in open('.//day9.txt').readlines()]
n, m = len(heightmap), len(heightmap[0])

def part_one():
    count = 0
    for i in range(n):
        for j in range(m):
            is_low_point = True
            point = heightmap[i][j]
            
            if i > 0:
                is_low_point &= point < heightmap[i-1][j]
            if i < n-1:
                is_low_point &= point < heightmap[i+1][j]
            if j > 0:
                is_low_point &= point < heightmap[i][j-1]
            if j < m-1:
                is_low_point &= point < heightmap[i][j+1]
            if is_low_point:
                count += point + 1
    print(count)
    
# part_one()

def part_two():
    basins, visited = [], set()
    for i in range(n):
        for j in range(m):
            point = heightmap[i][j]
            if point == 9 or (i, j) in visited:
                continue
            stack, basin = [(i, j)], set()
            while stack:
                x, y = stack.pop()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                basin.add((x, y))
                for dx, dy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= dx < n and 0 <= dy < m:
                        if heightmap[dx][dy] != 9 and (dx, dy) not in visited:
                            stack.append((dx, dy))
            basins.append(basin)
                
    basins.sort(key=len, reverse=True)
    # for basin in basins:
    #     print(len(basin))
    print(len(basins[0]) * len(basins[1]) * len(basins[2]))
            
part_two()