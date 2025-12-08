import os

path = os.path.dirname(os.path.abspath(__file__))

def compute(problems, operations):
  total = 0
  for i, problem in enumerate(problems):
    op = operations[i]
    subtotal = 0 if op == '+' else 1
    for elem in problem:
      if op == '+':
        subtotal += elem
      else:
        subtotal *= elem
    total += subtotal
    # print(subtotal)
  print(total)

def part_one():
  lines = [x.split() for x in open(path + '/day6.txt').readlines()]
  operations = lines.pop()
  m = len(lines[0])
  problems = [[] for _ in range(m)]
  for line in lines:
    for j, elem in enumerate(line):
      problems[j].append(int(elem))
  compute(problems, operations)

part_one()