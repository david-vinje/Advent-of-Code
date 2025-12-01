from queue import PriorityQueue

levels = [[int(y) for y in list(x.rstrip())] for x in open(path + '/day15.txt')]

# lav en kø
# smid første ting i køen
# lav et sæt med besøgte knuder
# sålænge køen ikke er tom:
    # tag en ting ud af køen
    # se evt. om det er mål
    # hvis den er besøgt, gå videre
    # ellers smid den i besøgte
    # kig på naboerne og læg dem i køen

def part_one(levels=levels):
    PQ = PriorityQueue()
    PQ.put((levels[0][0], (0, 0)))
    visited = set()
    n = len(levels) - 1
    while PQ:
        level, (x, y) = PQ.get()
        if (x, y) == (n, n):
            return level - levels[0][0]
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= dx <= n and 0 <= dy <= n:
                cost = level + levels[dx][dy]
                PQ.put((cost, (dx, dy)))
            
            
def inc(a, b):
    res = a+b
    if res > 9:
        return res - 9
    return res

def part_two():
    new_levels = []
    for i in range(5):
        for row in levels:
            new_row = []
            for j in range(5):
                new_row += [inc(x, j+i) for x in row]
            new_levels.append(new_row)
    return part_one(new_levels)
    
print(part_one())
print(part_two())