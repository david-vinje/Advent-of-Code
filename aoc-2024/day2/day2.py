reports = [
  [int(x) for x in report.split()]
  for report in open('./day2.txt')
]

def safety_check(levels):
  all_decreasing, all_increasing = True, True
  current = levels[0]
  for level in levels[1:]:
    if current <= level:
      all_decreasing = False
    if current >= level:
      all_increasing = False
    if not 0 < abs(current - level) < 4:
      return False
    current = level
  return all_decreasing or all_increasing
  
def part_one():
  count = 0
  for report in reports:
    if safety_check(report):
      count += 1
  print(count)
  

def problem_dampen(levels: list):
  for i, _ in enumerate(levels):
    dampened = levels[:i] + levels[i+1:]
    if safety_check(dampened):
      return True
  return False

def part_two():
  count = 0
  for report in reports:
    if safety_check(report):
      count += 1
    elif problem_dampen(report):
      count += 1
  print(count)

part_one()
part_two()