import os

path = os.path.dirname(os.path.abspath(__file__))

def solve(diagram=None, total=0, removable=False):
  if diagram is None:
    diagram = [list(x.rstrip()) for x in open(path + "/day4.txt").readlines()]
  total = 0
  n, m = len(diagram), len(diagram[0])
  for i, row in enumerate(diagram):
    for j, elem in enumerate(row):
      if elem != "@":
        continue
      count = 0
      for ix, jx in [
        (i - 1, j),
        (i, j - 1),
        (i + 1, j),
        (i, j + 1),
        (i - 1, j - 1),
        (i + 1, j + 1),
        (i + 1, j - 1),
        (i - 1, j + 1),
      ]:
        up_down = ix >= 0 and ix < n
        left_right = jx >= 0 and jx < n
        if up_down and left_right:
          neighbor = diagram[ix][jx]
          if neighbor == "@" or neighbor == 'x':
            count += 1

      if count < 4:
        if removable:
          diagram[i][j] = "."
        else:
          diagram[i][j] = "x"
        total += 1

  return diagram, total

def part_one():
  diagram, total = solve()
  # for row in diagram:
  #   print("".join(row))
  print(total)

def part_two(total=0, should_draw=False):
  diagram, subtotal = solve(removable=True)
  total = subtotal
  while subtotal > 0:
    diagram, subtotal = solve(diagram, subtotal, removable=True)
    total += subtotal
  # for row in diagram:
  #   print("".join(row))
  print(total)
  
part_one()
part_two()
