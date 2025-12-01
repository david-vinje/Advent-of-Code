from collections import Counter
from math import ceil

template, mapping = open(path + '/day14.txt').read().split('\n\n')
rules = dict()
for rule in mapping.split('\n'):
    pair, insertion = rule.split(' -> ')
    rules[pair] = insertion
    
def part_one(n):
    polymer = template
    for _ in range(n):
        n = len(polymer) - 1
        tmp = list(polymer)
        for i in range(n):
            pair = polymer[i] + polymer[i+1]
            insertion = rules[pair]
            tmp.insert(2*i+1, insertion)
        polymer = tmp
    count = Counter(polymer).most_common()
    most, least = count[0][1], count[-1][1]
    return most - least

def part_two(n):
    polymer = {}
    pairs = [template[i:i+2] for i in range(len(template)-1)]
    for pair in pairs:
        polymer.setdefault(pair, 0)
        polymer[pair] += 1
    for _ in range(n):
        tmp = {}
        for pair, count in polymer.items():
            a = pair[0] + rules[pair]
            b = rules[pair] + pair[1]
            tmp.setdefault(a, 0)
            tmp.setdefault(b, 0)
            tmp[a] += count
            tmp[b] += count
        polymer = {k: v for k, v in tmp.items()}
    counter = {}
    for pair, count in polymer.items():
        a, b = pair
        counter.setdefault(a, 0)
        counter.setdefault(b, 0)
        counter[a] += count
        counter[b] += count
    counter = sorted([ceil(count/2) for count in counter.values()])
    return counter[-1] - counter[0]

print(part_two(10), part_two(40))
