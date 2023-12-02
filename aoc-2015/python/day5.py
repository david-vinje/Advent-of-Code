# read input
lines = open('aoc-2015/input/day5.txt').readlines()

# part one
def is_nice(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    appeared_twice = False
    prev_letter = ''
    for c in list(s):
        if c in vowels:
            vowel_count += 1
        if prev_letter == c:
            appeared_twice = True
        prev_letter = c
    if vowel_count < 3:
        return False
    if not appeared_twice:
        return False
    forbidden_words = ['ab', 'cd', 'pq', 'xy']
    for word in forbidden_words:
        if word in s:
            return False
    return True

count = sum([1 if is_nice(s) else 0 for s in lines])
print(count)

# part two
def is_nicer(s):
    is_nice = False
    for i, _ in enumerate(s):
        for j, _ in enumerate(s[i+1:-1]):
            j0 = i+j+2
            if s[i:i+2] == s[j0:j0+2]:
                is_nice = True
    if not is_nice:
        return False
    is_nice = False
    for i, _ in enumerate(s[0:-2]):
        if s[i] == s[i+2]:
            is_nice = True
            break
    return is_nice

count = sum([1 if is_nicer(s) else 0 for s in lines])
print(count)