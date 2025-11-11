x, y, dir = 0, 0, 0
map = []
for i, row in enumerate(open('.//day6.txt')):
  map.append(list(row))
  for j, elem in enumerate(row):
    if elem == '^':
      x, y = i, j
n = len(map)
visited = {(x, y)}
  
def move(x, y, dir):
  if dir == 0:
    x -= 1
  elif dir == 1:
    y += 1
  elif dir == 2:
    x += 1
  else:
    y -= 1
  return x, y

def print_map():
  s = ""
  for r in range(0, n):
    for c in range(0, n):
      s += map[r][c]
    s += '\n'
  print(s)

def part_one():
  dir = 0
  x, y = visited.pop()
  visited.add((x, y))
  while True:
    nx, ny = move(x, y, dir)
    if not (0 <= nx < n and 0 <= ny < n):
      break
    if map[nx][ny] == '#':
      dir = (dir+1) % 4
    x, y = move(x, y, dir)
    visited.add((x, y))
  print(len(visited))

part_one()  

def is_loop(map, x, y):
  dir = 0
  visited = {(x, y, dir)}
  while True:
    nx, ny = move(x, y, dir)
    if not (0 <= nx < n and 0 <= ny < n):
      # print_map()
      return False
    while map[nx][ny] == '#' or map[nx][ny] == 'X':
      dir = (dir+1) % 4
      nx, ny = move(x, y, dir)
    x, y = move(x, y, dir)
    map[x][y] = '^'
    if (x, y, dir) in visited:
      # print_map()
      return True
    visited.add((x, y, dir))
  
def part_two(x, y):
  count = 0
  for (vx, vy) in visited:
    map[vx][vy] = 'X'
    # print(vx, vy)
    if is_loop(map, x, y):
      count += 1
    map[vx][vy] = '.'
  print(count)
      
part_two(x, y)  