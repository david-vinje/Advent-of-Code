import re

lines = open('./day3.txt')
total = 0
enabled = True
for line in lines:
  matches = re.findall("(mul\([0-9]*,[0-9]*\)|don't|do?)", line)
  for match in matches:  
    if match == "don't":
      enabled = False
    elif match == 'do':
      enabled = True
    elif enabled:
      mults = [int(x) for x in match.lstrip("mul(").rstrip(")").split(",")]
      total += mults[0] * mults[1]
      print(mults, total)
print(total)