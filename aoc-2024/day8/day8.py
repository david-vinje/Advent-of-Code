import os

path = os.path.dirname(os.path.abspath(__file__))

chart = []
antennas = {}
for i, row in enumerate(open(path + '/day8.txt')):
  tmp = []
  for j, elem in enumerate(row.strip()):
    tmp.append(elem)
    if elem == '#':
      elem = '.'
    if elem != '.':
      if elem not in antennas.keys():
        antennas[elem] = []
      antennas[elem] += [(j, i)]
  chart.append(tmp)
n = len(chart)
anti_nodes = set()

def mark(x, y):
  if 0 <= x < n and 0 <= y < n:
    if chart[x][y] == '.':
      chart[x][y] = '#'
    anti_nodes.add((x, y))

""" Part One """
for locations in antennas.values():
  for i, (y1, x1) in enumerate(locations):
    for (y2, x2) in locations[i+1:]:
      dx = abs(x1 - x2)
      dy = abs(y1 - y2)
      if x1 < x2:
        if y1 < y2:
          mark(x1 - dx, y1 - dy)
          mark(x2 + dx, y2 + dy)
        else:
          mark(x1 - dx, y1 + dy)
          mark(x2 + dx, y2 - dy)
      else:
        if y1 < y2:
          mark(x1 + dx, y1 - dy)
          mark(x2 - dx, y2 + dy)
        else:
          mark(x1 + dx, y1 + dy)
          mark(x2 - dx, y2 - dy)
           
""" Part Two """ 
for locations in antennas.values():
  for i, (y1, x1) in enumerate(locations):
    for (y2, x2) in locations[i+1:]:
      anti_nodes.add((x1, y1))
      anti_nodes.add((x2, y2))
      dx = abs(x1 - x2)
      dy = abs(y1 - y2)
      if x1 < x2:
        if y1 < y2:
          x = x1 - dx
          y = y1 - dy
          mark(x, y)
          while 0 <= x and 0 <= y:
            x -= dx
            y -= dy
            mark(x, y)
          x = x2 + dx
          y = y2 + dy
          mark(x, y)
          while x < n and y < n:
            x += dx
            y += dy
            mark(x, y)
        else:
          x = x1 - dx
          y = y1 + dy
          mark(x, y)
          while 0 <= x and y < n:
            x -= dx
            y += dy
            mark(x, y)
          x = x2 + dx 
          y = y2 - dy
          mark(x, y)
          while x < n and y >= 0:
            x += dx
            y -= dy
            mark(x, y)
      else:
        if y1 < y2:
          x = x1 + dx
          y = y1 - dy
          mark(x, y)
          while x < n and y >= 0:
            x += dx
            y -= dy
            mark(x, y)
          x = x2 - dx
          y = y2 + dy
          mark(x, y)
          while x >= 0 and y < n:
            x -= dx
            y += dy
            mark(x, y)
        else:
          x = x1 + dx
          y = y1 + dy
          mark(x, y)
          while x < n and y < n:
            x += dx
            y += dy
            mark(x, y)
          x = x2 - dx
          y = y2 - dy
          mark(x, y)
          while x >= 0 and y >= 0:
            x -= dx
            y -= dy
            mark(x, y)
        
res = '\n'
for row in chart:
  res += ''.join(row) + '\n'
print(res)
ans = """
##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
"""

print(len(anti_nodes), ans == res)
