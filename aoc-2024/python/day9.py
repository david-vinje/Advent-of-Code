disk_map = [int(x) for x in list(open('./input/day9.txt').read())]
id = 0
i = 0
n = len(disk_map)
s = []

while i < n - 1:
  file_size = disk_map[i]
  i += 1
  free_space = disk_map[i]
  i += 1
  for j in range(file_size):
    s.append(str(id))
  for j in range(free_space):
    s.append('.')
  id += 1
  
file_size = disk_map[i]
for j in range(file_size):
  s += [str(id)]
# print(''.join(s)) 

left, right = 0, len(s) - 1
while left < right:
  while s[left] != '.':
    left += 1
  while s[right] == '.':
    right -= 1
  s[left] = s[right]
  s[right] = '.'
s[right] = s[left]
s[left] = '.'
# print(''.join(s))

checksum = 0
for i, id in enumerate(s):
  if id == '.':
    break
  mult = i * int(id)
  checksum += mult
  # print(i, '*', id, '=', mult, checksum)
print(checksum)