import os

path = os.path.dirname(os.path.abspath(__file__))

S, E = (0,0), (0,0)
map = []
for i, row in enumerate(open(path + '/day16.txt')):
  map.append(list(row.strip()))
  for j, elem in enumerate(row):
    if elem == 'S':
      S = (i, j)
    elif elem == 'E':
      E = (i, j)

from queue import PriorityQueue

def part_one():
  PQ = PriorityQueue()
  PQ.put((0, S, True, [], 0))
  visited = set()
  while PQ:
    cost, (i, j), horizontal, path, turns = PQ.get()
    if (i, j) in visited:
      continue
    visited.add((i, j))
    if horizontal:
      for y in [j+1, j-1]:
        pos = (i, y)
        new_path = path + [pos]
        if horizontal:
          new_cost = cost + 1
          if pos == E:
            return new_cost, new_path
          if map[i][y] != '#':
            PQ.put((new_cost, pos, True, new_path, turns))
    else:
      for x in [i+1, i-1]:
        pos = (x, j)
        new_path = path + [pos]
        if not horizontal:
          new_cost = cost + 1
          if pos == E:
            return new_cost, new_path
          if map[x][j] != '#':
            PQ.put((new_cost, pos, False, new_path, turns))
        

    
cost, path = part_one()
for i, row in enumerate(map):
  for j, elem in enumerate(row):
    if (i, j) in path:
      map[i][j] = 'X'
  print(row)
print(cost)