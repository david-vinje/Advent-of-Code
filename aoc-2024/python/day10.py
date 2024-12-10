chart = []
trailheads = []
for i, row in enumerate(open('./input/day10.txt')):
  tmp = [] 
  for j, elem in enumerate(row.strip()):
    if elem == '.':
      elem = -1
    else:
      elem = int(elem)
    tmp.append(elem)
    if elem == 0:
      trailheads.append((i, j))
  chart.append(tmp)
n = len(chart)
# print(chart)
# print(trailheads)

scores = []
for trailhead in trailheads:
  queue = [trailhead]
  score = 0
  visited = set()
  while queue:
    row, col = queue.pop()
    elem = chart[row][col]
    if elem == 9: score += 1
    for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
      if 0 <= i < n and 0 <= j < n:
        neighbor = chart[i][j]
        if neighbor == elem+1 and (i, j) not in visited:
          queue.append((i, j))
          visited.add((i, j))
  scores.append(score)
# print(scores)
print(sum(scores))

def string(i, j):
  return '(' + str(i) + ',' + str(j) + ')'

def find_rating(row, col):
  trails = set()
  def backtrack(row, col, trail: list):
    elem = chart[row][col]
    if elem == 9:
      trails.add(trail)
      return
    for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
      if 0 <= i < n and 0 <= j < n:
        neighbor = chart[i][j]
        if neighbor == elem+1:
          backtrack(i, j, trail + string(i, j))
  backtrack(row, col, string(row, col))
  return len(trails)
  
ratings = []
for (i, j) in trailheads:
  rating = find_rating(i, j)
  ratings.append(rating)
# print(ratings)
print(sum(ratings))


