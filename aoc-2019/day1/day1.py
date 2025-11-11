import os
path = os.path.dirname(os.path.abspath(__file__))

masses = [int(x) for x in open(path + '/day1.txt')]
#masses = [12, 14, 1969, 100756]

def part_one():
  total = 0
  for mass in masses:
    fuel_requirement = mass // 3 - 2
    total += fuel_requirement
  print(total)

def compute_fuel_requirement(requirement, total):
  requirement = requirement // 3 - 2
  if (requirement < 0):
    return total
  total += requirement
  return compute_fuel_requirement(requirement, total)

#masses = [14, 1969, 100756]

def part_two():
  total = 0
  for mass in masses:
    fuel_requirement = compute_fuel_requirement(mass, 0)
    total += fuel_requirement
  print(total)

#part_one()
part_two()