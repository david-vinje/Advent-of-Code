lines = [x.rstrip('\n').split(' ') for x in open('aoc-2015/input/day7.txt')]
wires = {}
read = set()
i = 0

while len(read) < len(lines):
    line = lines[i]
    i += 1
    if i == len(lines):
        i = 0
    instruction = ''.join(line)
    if instruction in read:
        continue
    val1, op, val2, key = line[0], line[1], line[2], line[-1]
    if op == '->':
        if val1.isdigit():
            wires[key] = int(val1)
        elif val1 in wires:
            wires[key] = wires[val1]
    elif op == 'AND':
        if val1 not in wires or val2 not in wires:
            continue
        wires[key] =  wires[val1] & wires[val2]
    elif op == 'OR':
        if val1 not in wires or val2 not in wires:
            continue
        wires[key] =  wires[val1] | wires[val2]
    elif op == 'LSHIFT':
        if val1 not in wires:
            continue
        wires[key] = wires[val1] << int(val2)
    elif op == 'RSHIFT':
        if val1 not in wires:
            continue
        wires[key] = wires[val1] >> int(val2)
    else:
        val = line[1]
        if val not in wires:
            continue
        val = ~wires[val] + 2**16
        wires[key] = val 
    read.add(instruction)
    
print(wires) if 'a' not in wires else print(wires['a'])