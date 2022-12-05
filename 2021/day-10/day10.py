
#filename = 'demo-10.txt'
filename = 'input-10.txt'

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

checker_score = 0
corrupted = []
completer_scores = []

CHECKER_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
COMPLETER_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}
OPEN = ['(', '[', '{', '<']
#CLOSE = [')', ']', '}', '>']
CLOSING = {'(': ')', '[': ']', '{': '}', '<': '>'}

for line in lines:
    valid = True
    stack = []
    for ch in line:
        if ch in OPEN:
            stack.append(ch)
        else:
            if ch == CLOSING[stack[-1]]:
                stack.pop(-1)
            else:
                checker_score += CHECKER_POINTS[ch]
                corrupted.append(ch)
                valid = False
                break
    if valid:
        # autocomplete
        line_score = 0
        additions = []
        stack.reverse()
        for ch in stack:
            additions.append(CLOSING[ch])
            line_score *= 5
            line_score += COMPLETER_POINTS[CLOSING[ch]]
        #print(line, " -> ", additions, " : ", line_score)
        completer_scores.append(line_score)

print(f"Part 1 total score: {checker_score}")


completer_scores.sort()
num = len(completer_scores)
side = (num - 1) // 2


print(f"Part 2 total score: {completer_scores[side]}")
