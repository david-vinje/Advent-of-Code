lines = [list(x.rstrip()) for x in open('.//day10.txt').readlines()]
opening = {'[', '(', '{', '<'}
pairs = {
    ']': '[',
    '}': '{',
    ')': '(',
    '>': '<'
}
def part_one():
    total = 0
    scoring = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    for line in lines:
        stack = []
        for chunk in line:
            if chunk in opening:
                stack.append(chunk)
            else:
                opener = stack.pop()
                if pairs[chunk] != opener:
                    total += scoring[chunk]
                    break
    print(total)
    
def part_two():
    scores = []
    scoring = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    for line in lines:
        stack = []
        corrupted = False
        for chunk in line:
            if chunk in opening:
                stack.append(chunk)
            else:
                opener = stack.pop()
                if pairs[chunk] != opener:
                    corrupted = True
                    break
        if not corrupted:
            score = 0
            while stack:
                chunk = stack.pop()
                score *= 5
                score += scoring[chunk]
            scores.append(score)
    scores.sort()
    m = int(len(scores)/2)
    print(scores[m])

part_one()
part_two()