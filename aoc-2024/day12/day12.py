garden = [list(row.strip()) for row in open('.//day12.txt')]
visited = set()
n = len(garden)

def search(i, j):
  queue = [(i, j)]
  plant = garden[i][j]
  region = {(i, j)}
  while queue:
    i, j = queue.pop()
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
      if 0 <= x < n and 0 <= y < n \
        and garden[x][y] == plant \
        and (x, y) not in region:
          queue.append((x, y))
          region.add((x, y))
  return region

def get_perimeter(region):
  perimeter = []
  for (i, j) in region:
    for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
      if (x, y) not in region:
        perimeter.append((x, y))
  return perimeter

def get_sides(perimeter: list):
  # count = 0
  sides = set()
  visited = set()
  for (i, j) in region:
    queue = [(i, j)]
    while queue:
      i, j = queue.pop()
      going_sideways = False
      for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if (x, y) in perimeter and (x, y) not in visited:
          queue.append((x, y))
          visited.add((x, y))
          going_sideways = True
      if going_sideways: 
        continue
      for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if (x, y) not in perimeter:
          sides.add((x, y))
  return sides

total = 0
for i, row, in enumerate(garden):
  for j, plant in enumerate(row):
    if (i, j) not in visited:
      region = search(i, j)
      visited.update(region)
      perimeter = get_perimeter(region)
      # price = len(region) * len(perimeter)
      sides = get_sides(perimeter)
      price = len(region) * len(sides)
      print(plant, len(sides), sides)
      total += price
print(total)
