floors = open('.//day1.txt').readline()

count = 0
for floor in floors:
  if floor == '(':
    count += 1
  else:
    count -=1
print(count)

count = 0
for i, floor in enumerate(floors):
  if floor == '(':
    count += 1
  else:
    count -=1
  if count < 0:
    print(i+1)
    break