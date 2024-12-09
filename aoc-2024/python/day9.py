disk_map = [int(x) for x in list(open('./input/day9.txt').read())]
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
  
<<<<<<< HEAD
=======

# def part_two(s):
#   while chunks:
#     file_size, id, chunk_position = chunks.pop()
#     for i, (space, position) in enumerate(free_spaces):
#       if file_size <= space:
#         print(''.join(s))
#         print(free_spaces)
#         chunk = s[chunk_position-file_size : chunk_position]
#         # print(chunk)
#         # empty = s[position : position + file_size]
#         s[position : position + file_size] = [id] * file_size
#         s[chunk_position-file_size : chunk_position] = ['.'] * file_size
#         # free_spaces[i] = (space - file_size, position + file_size)
#         break
#   print(''.join(s)) 
#   print(free_spaces)
#   compute(s.copy())

>>>>>>> 8eaef424a5d6b92f2d8d483f8fece6134e78681c
def part_two(s):
  n = len(s)
  j = 0
  while chunks:
    file_size, id, chunk_end = chunks.pop()
    chunk_start = chunk_end - file_size
    i = j
    space_found = False
    first_found = False
    while i < chunk_start and not space_found:
      while i < chunk_start and s[i] != '.':
        i += 1
      if not first_found:
        j = i
        first_found = True
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