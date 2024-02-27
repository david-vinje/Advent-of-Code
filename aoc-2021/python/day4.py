lines = open('./input/day4.txt').read().split('\n\n')

numbers_drawn = [int(number) for number in lines[0].split(',')]

class Number:
    def __init__(self, value):
        self.drawn = False
        self.value = value

boards = [
    [
        [Number(int(number)) for number in row.split()] 
        for row in board.split('\n')
    ] for board in lines[1:]
]

def compute_score(board: list[list[Number]]):
    score = 0
    for row in board:
        for number in row:
            if not number.is_drawn:
                score += number.value
    return score

n = len(boards[0][0])

def is_winner(board):
    for row in board:
        drawns = [number.drawn for number in row]
        if all(drawns):
            return True
    columns = [[board[i][j] for i in range(n)] for j in range(n)]
    for column in columns:
        drawns = [number.drawn for number in column]
        if all(drawns):
            return True
    return False

def compute_score(board):
    score = 0
    for row in board:
        for number in row:
            if not number.drawn:
                score += number.value
    return score

def part_one():
    for number_drawn in numbers_drawn:
        for board in boards:
            for row in board:
                for number in row:
                    if number.value == number_drawn:
                        number.drawn = True
                        if is_winner(board):
                            return compute_score(board) * number_drawn   
print(part_one())

