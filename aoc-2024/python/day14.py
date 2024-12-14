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
  for x in open('./input/day14.txt')
]

for robot in robots:
  (x, y), _ = robot
  tiles[y][x] += 1
  
def move(robot):
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

for j in range(200):
  for i, robot in enumerate(robots):
    robots[i] = move(robot) 
  if j > 99:
    f = open("./trees/{j}.txt".format(j=j), "w")
    f.write(tiles_to_str())
    f.close()

    
res = tiles_to_str()
ans = """
...........
...........
...........
...........
...........
...........
...........
"""
print(res)
print(res == ans)

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

safety_factor = 1
for count in counts:
  safety_factor *= count
print(safety_factor)
