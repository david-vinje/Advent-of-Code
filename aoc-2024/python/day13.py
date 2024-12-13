from math import ceil

raw_machines = open('./input/day13.txt').read().split('\n\n')
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
  # print(ax, ay, bx, by, tx, ty)
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
  # if cost:
  #   print(cost)
  return cost

total = 0
for machine in machines:
  tokens = min_tokens(machine, 101)
  # tokens = min_tokens(machine)
  if tokens:
    total += tokens
print(total)
  