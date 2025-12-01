import os

path = os.path.dirname(os.path.abspath(__file__))

disk_map = [int(x) for x in list(open(path + '/day9.txt').read())]
id = 0
i = 0
n = len(disk_map) - 1
s = []
free_spaces = []
chunks = []

while i < n:
  file_size = disk_map[i]
  i += 1
  free_space = disk_map[i]
  i += 1
  for j in range(file_size):
    s.append(str(id))
  chunks.append((file_size, str(id), len(s)))
  free_spaces.append((free_space, len(s)))
  for j in range(free_space):
    s.append('.')
  id += 1

file_size = disk_map[i]
for j in range(file_size):
  s += [str(id)]
chunks.append((file_size, str(id), len(s)))
# print(''.join(s)) 

def compute(s):
  checksum = 0
  for i, id in enumerate(s):
    if id == '.': 
      continue
    mult = i * int(id)
    checksum += mult
    # print(i, '*', id, '=', mult, checksum)
  print(checksum)

def part_one(s):
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
  compute(s.copy())

def part_two(s):
  j = 0
  while chunks:
    file_size, id, chunk_end = chunks.pop()
    chunk_start = chunk_end - file_size
    i = j
    space_found, first_space = False, False
    while i < chunk_start and not space_found:
      while i < chunk_start and s[i] != '.':
        i += 1
      if not first_space:
        j = i
        first_space = True
      space = 0
      while i < chunk_start and s[i] == '.' :
        space += 1
        if file_size == space:
          # print(''.join(s))
          empty_start = i-file_size+1
          empty_end = empty_start + file_size
          s[empty_start : empty_end] = [id] * file_size
          s[chunk_start : chunk_end] = ['.'] * file_size
          space_found = True
          break
        i += 1
  # print(''.join(s)) 
  compute(s.copy())
     

part_one(s.copy())
part_two(s.copy())