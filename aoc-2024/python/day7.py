from itertools import combinations
equations = []
for line in open('./input/day7.txt'):
  test, nums = line.split(': ')
  test = int(test)
  nums = [int(num) for num in nums.split()]
  equations.append([test, nums])
  
sum_total = 0
for equation in equations:
  test, nums = equation
  totals = [nums[0]]
  for num in nums[1:]:
    tmp = []
    for total in totals:
      tmp.append(total + num)
      tmp.append(total * num)
      tmp.append(int(str(total) + str(num)))
    totals = tmp
  if test in totals:
    sum_total += test
    # print(test)
print(sum_total)