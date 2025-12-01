import os

path = os.path.dirname(os.path.abspath(__file__))

raw_map, instructions = open(path + '/day15.txt').read().split("\n\n")

map, robot = [], (0, 0)
for i, row in enumerate(raw_map.split('\n')):
  map.append(list(row))
  for j, elem in enumerate(row):
    if elem == '@':
      robot = (i, j)

def move(x, y, inst):
  if inst == '<':
    return (x, y-1)
  elif inst == '>':
    return (x, y+1)
  elif inst == '^':
    return (x-1, y)
  elif inst == 'v':
    return (x+1, y)

def swap(x, y, inst):    
  tmp = map[x][y]
  i, j = move(x, y, inst)
  map[x][y] = map[i][j]
  map[i][j] = tmp

def can_move(i, j, inst):
  x, y = move(i, j, inst)
  elem = map[x][y]
  if elem == '#':
    return False
  elif elem == 'O':
    if can_move(x, y, inst):
      swap(x, y, inst)
      return True
  else:
    return True

i, j = robot
for k, inst in enumerate(instructions):
  if inst == '\n': continue
  if can_move(i, j, inst):
    swap(i, j, inst)
    i, j = move(i, j, inst)
  
def str_map():
  s = '\n'
  for row in map:
    s += ''.join(row)
    s += '\n'
  return s

def compute():
  total = 0
  for i, row in enumerate(map):
    for j, elem in enumerate(row):
      if elem == 'O':
        total += 100*i + j
  print(total) 

res = str_map()
ans = """
##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
"""
print(res)
print(res == ans)

raw_map, instructions = open(path + '/day15.txt').read().split("\n\n")
map, robot = [], (0, 0)
for i, row in enumerate(raw_map.split('\n')):
  map.append(list(row))
  for j, elem in enumerate(row):
    if elem == '@':
      robot = (i, j)