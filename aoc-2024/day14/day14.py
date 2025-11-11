# n, m = 7, 11
n, m = 103, 101
tiles = []
for _ in range(n):
  row = []
  for _ in range(m):
    row.append(0)
  tiles.append(row)
  
robots = [
  [
    [int(z) for z in y.split('=')[1].split(',')]
    for y in x.split()
  ]
  for x in open('.//day14.txt')
]

for robot in robots:
  (x, y), _ = robot
  tiles[y][x] += 1
    
def move(robot, j):
  global highest
  (x, y), (vx, vy) = robot
  dx, dy = (x+vx) % m, (y+vy) % n
  tiles[y][x] = max(0, tiles[y][x]-1)
  tiles[dy][dx] += 1
  return (dx, dy), (vx, vy)

def tiles_to_str():
  s = '\n'
  for row in tiles:
    for tile in row:
      if tile == 0:
        s += '.'
      else:
        s += str(tile)
    s += '\n'
  return s

def tiles_to_str():
  s = '\n'
  for row in tiles:
    for tile in row:
      if tile == 0:
        s += '.'
      else:
        s += str(tile)
    s += '\n'
  return s
    
# res = tiles_to_str()
# ans = """
# ...........
# ...........
# ...........
# ...........
# ...........
# ...........
# ...........
# """
# print(res)
# print(res == ans)

counts = [0, 0, 0, 0]
x, y = int(n/2), int(m/2)
for i, row in enumerate(tiles):
  if i == x: continue
  for j, tile in enumerate(row):
    if j == y or tiles[i][j] == 0: continue
    if i < x:
      if j < y:
        counts[0] += tiles[i][j]
      else:
        counts[1] += tiles[i][j]
    else:
      if j < y:
        counts[2] += tiles[i][j]
      else:
        counts[3] += tiles[i][j]

def compute_safety():
  safety_factor = 1
  for count in counts:
    safety_factor *= count
  return safety_factor


for j in range(1, 7624):
  for i, robot in enumerate(robots):
    robots[i] = move(robot, j) 
  safety_factor = compute_safety()
  if j > 7622:    
    print(tiles_to_str())
    print(j)
