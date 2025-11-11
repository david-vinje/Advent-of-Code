from math import ceil

raw_machines = open('.//day13.txt').read().split('\n\n')
machines = []
for raw_machine in raw_machines:
  machine = []
  raw_machine = raw_machine.split('\n')
  for i, raw_line in enumerate(raw_machine):
    line = raw_line.split(': ')[1]
    for elem in line.split(', '):
      elem = int(''.join(list(filter(str.isdigit, elem))))
      # if i == 2:
      #   elem += 10000000000000
      #   print(elem)
      machine.append(elem)
  machines.append(machine)

def min_tokens(machine, ceiling = None):
  cost = None
  ax, ay, bx, by, tx, ty = machine
  AN = max(ceil(tx / ax), ceil(ty / ay))
  BN = max(ceil(tx / bx), ceil(ty / by))
  if ceiling:
    AN = min(AN, ceiling)
    BN = min(BN, ceiling)
  for an in range(AN):
    for bn in range(BN):
      if an*ax + bn*bx == tx and an*ay + bn*by == ty:
        price = an*3 + bn
        if not cost:
          cost = price
        elif price < cost:
          cost = price
  return cost


import cvxpy as cp
import numpy as np

total = 0

def linprog(machine):
  moveX = np.array([machine[0], machine[2]])
  moveY = np.array([machine[1], machine[3]])

  SelectionX = cp.Variable(len(moveX), integer=True)
  SelectionY = cp.Variable(len(moveY), integer=True)

  constraints = [
      SelectionX >= 0,
      SelectionY >= 0,
      SelectionX @ moveX == machine[4],
      SelectionY @ moveY == machine[5],
  ]

  objFunction = 3 * cp.sum(SelectionX) + 1 * cp.sum(SelectionY)

  problem = cp.Problem(cp.Minimize(objFunction), constraints)

  problem.solve(solver=cp.GLPK_MI)
  if problem.solution.status == 'optimal':
    tokens = int(SelectionX.value[0]*3 + SelectionX.value[1])
    # total += tokens
    print(problem.value)
    return tokens    

for machine in machines:
  tokens = min_tokens(machine)
  if tokens:
    print(tokens, linprog(machine))
  
