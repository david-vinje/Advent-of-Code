connections = [x.rstrip().split('-') for x in  open('.//day12.txt').readlines()]
map: dict[str, list[str]] = {}
for a, b in connections:
    map.setdefault(a, [])
    map.setdefault(b, [])
    map[a].append(b)
    map[b].append(a)
    
def part_one():
    paths = set()
    def backtrack(cave, path):
        if cave == 'end':
            paths.add(path)
            return
        if path in paths:
            return
        for neighbor in map[cave]:
            if neighbor == 'start' or (neighbor.islower() and neighbor in path):
                continue
            backtrack(neighbor, path + '-' + neighbor)
    backtrack('start', 'start')
    print(len(paths))
    
def part_two():
    paths = set()
    def backtrack(cave, path, chosen):
        if cave == 'end':
            paths.add(path)
            return
        if path in paths:
            return
        for neighbor in map[cave]:
            if neighbor == 'start':
                continue
            if neighbor.islower():
                count = path.count(neighbor)
                if count == 2 or (count == 1 and chosen != neighbor):
                    continue
            backtrack(neighbor, path + ',' + neighbor, chosen)
    small_caves = set()
    for a, b in connections:
        if a.islower():
            small_caves.add(a)
        if b.islower():
            small_caves.add(b)
    for chosen in small_caves:
        backtrack('start', 'start', chosen)
    print(len(paths))

# part_one()
part_two()