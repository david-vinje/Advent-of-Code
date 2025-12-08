import os
path = os.path.dirname(os.path.abspath(__file__))

def create_diagram():
  diagram = [list(x.rstrip()) for x in open(path + '/day7.txt').readlines()]
  start = diagram[0].index('S')
  diagram[1][start] = '|'
  return diagram

def right_split(diagram, i, j):
  diagram[i][j+1] = '|'
  return diagram

def left_split(diagram, i, j, going_left=True):
  diagram[i][j-1] = '|'
  return diagram

def split(diagram, i, j, going_left=True):
  return right_split(left_split(diagram, i, j), i, j)

def alternate(diagram, i, j, going_left=True):
  if going_left:
    return left_split(diagram, i, j)
  return right_split(diagram, i, j)


def solve(diagram, split=split):
  count = 0
  for i, row in enumerate(diagram):
    for j, elem in enumerate(row):
      if elem == '^' and diagram[i-1][j] == '|':
        going_left = count % 2 == 0
        count += 1
        diagram = split(diagram, i, j, going_left)
      elif i > 0 and diagram[i-1][j] == '|':
        diagram[i][j] = '|'
  print(count)
  return diagram

def part_one():
  diagram = solve(create_diagram())
  for row in diagram:
      print(''.join(row))
      
def part_two():
  digram = solve(create_diagram(), split=left_split)
  for row in digram:
      print(''.join(row))
  digram = solve(create_diagram(), split=alternate)
  for row in digram:
      print(''.join(row))

part_one()
part_two()